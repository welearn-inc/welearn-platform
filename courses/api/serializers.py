from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from courses.models import Course
from courses.models import Module
from accounts.api.serializers import UserPublicSerializer

class ModuleSerializer(serializers.ModelSerializer):
  class Meta:
      model = Module
      fields = ['id','title']

class CoursesSerializer(serializers.ModelSerializer):
  uri  = serializers.SerializerMethodField(read_only=True)
  user = UserPublicSerializer(read_only=True)
  modules = serializers.SerializerMethodField()

  class Meta:
    model = Course
    fields = [
     'name','slug','image','headline',
     'description','category','subcategory',
     'published_date', 'modified_date',
     'modules',
     'featured','active',
     'user',
     'uri',
     ]

  def get_modules(self, obj):
    serializer = ModuleSerializer(many=True)
    return serializer.data

  def get_uri(self, obj):
    request = self.context.get('request')
    return api_reverse('api-courses:detail', kwargs={"slug": obj.slug}, request=request)

  def validate(self, data):
    description = data.get("description", None)
    if description == "":
        description = None
    image = data.get("image", None)
    if description is None and image is None:
        raise serializers.ValidationError("Description or image is required.")
    return data
