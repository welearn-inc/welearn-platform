import datetime

from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from rest_framework_jwt.settings import api_settings

jwt_payload_handler           = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler            = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class UserPublicSerializer(serializers.ModelSerializer):
  uri = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = User
    fields = ['id', 'username', 'uri']
    
  def get_uri(self, obj):
      request = self.context.get('request')
      return api_reverse("api-user:detail", kwargs={"username": obj.username}, request=request)


class UserRegisterSerializer(serializers.ModelSerializer):
  password         = serializers.CharField(style={'input_type': 'password'}, write_only=True)
  password2        = serializers.CharField(style={'input_type': 'password'}, write_only=True)
  token            = serializers.SerializerMethodField(read_only=True)
  expires          = serializers.SerializerMethodField(read_only=True)
  message          = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model   = User
    fields  = [
      'username',
      'password',
      'password2',
      'token',
      'expires',
      'message',
    ]
    extra_kwargs = {'password':{'write_only':True}}

  def validate_username(self, value):
    qs = User.objects.filter(username__iexact=value)
    if qs.exists():
      raise serializers.ValidationError("User with this email already exists")
    return value

  def validate(self, data):
    password  = data.get('password')
    password2 = data.pop('password2')

    if password != password2:
      raise serializers.ValidationError("Passwords must match")
    return data

  def get_token(self, obj):
      user    = obj
      payload = jwt_payload_handler(user)
      token   = jwt_encode_handler(payload)
      return token

  def get_expires(self, obj):
      return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

  def get_message(self, obj):
      return "Thank you for registering. Please verify your email before continuing."

  def create(self, validated_data):
    user = User(**validated_data)
    password = validated_data.get('password')

    if user:
      user.set_password(password)
      user.is_active = False
      user.save()
    return user