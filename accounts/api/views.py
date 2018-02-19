from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q

from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from .permissions import AnonPermissionOnly
from .serializers import UserRegisterSerializer

jwt_payload_handler           = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler            = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler  = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()

class AuthAPIView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request, *args, **kwargs):
    if request.user.is_authenticated():
      return Response({'detail': 'You are already authenticated'}, status=400)
 
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    qs = User.objects.filter(
        Q(username__iexact=username)|
        Q(email__iexact=username)
      ).distinct()
    user_obj = qs.first() 
    if qs.first().check_password(password):
      user = user_obj
      payload = jwt_payload_handler(user)
      token = jwt_encode_handler(payload)
      response = jwt_response_payload_handler(token, user, request=request)
      return Response(response)
    return Response({"detail": "Invalid credentials"}, status=401)

class RegisterAPIView(generics.CreateAPIView):
  serializer_class    = UserRegisterSerializer
  permission_classes  = [AnonPermissionOnly]

  def get_queryset(self):
    return User.objects.all()

  def get_serializer_context(self, *args, **kwargs):
    return {"request": self.request}