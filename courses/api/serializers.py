from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from courses.models import Course
from courses.models import Module

from accounts.models import Student
from accounts.models import Teacher

from accounts.api.serializers import UserPublicSerializer

class ModuleSerializer(serializers.ModelSerializer):
  class Meta:
      model  = Module
      fields = ['id', 'name']

class StudentSerializer(serializers.ModelSerializer):
  fullname = serializers.CharField(source='student.fullname')
  class Meta:
      model  = Student
      fields = ['id', 'fullname']

# class TagListSerializer(serializers.Serializer):
#     id   = serializers.IntegerField()
#     name = serializers.CharField()

class CoursesSerializer(serializers.ModelSerializer):
  modules  = ModuleSerializer(many=True, read_only=True)
  
  teacher  = serializers.StringRelatedField(read_only=True)
  students = StudentSerializer(many=True, read_only=True)
  
  user     = UserPublicSerializer(read_only=True)
  uri      = serializers.SerializerMethodField(read_only=True)
  # tags     = serializers.ListField(child=TagListSerializer())

  
  class Meta:
    model = Course
    fields = [
     'name','slug','headline','description','category','image','video',
     'pricing','language','level',
     'goals', 'benefits',
     'created_date', 'modified_date',
     'modules',
     'featured','active',
     'students','teacher',
     # 'tags',
     'user',
     'uri'
    ]

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
