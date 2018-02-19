from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from courses.api.serializers import CoursesSerializer

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
  uri     = serializers.SerializerMethodField(read_only=True)
  courses = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = User
    fields = ['id', 'username', 'uri', 'courses']

  def get_uri(self, obj):
    request = self.context.get('request')
    return api_reverse("api-user:detail", kwargs={"username": obj.username}, request=request)

  def get_courses(self, obj):
    request = self.context.get('request')
    limit = 3
    if request:
      limit_query = request.GET.get('limit')
      try:
        limit = int(limit_query)
      except:
        pass
    qs = obj.course_set.all().order_by("-timestamp")
    data = {
      'uri': self.get_uri(obj) + "courses/",
      'last': CoursesSerializer(qs.first(), context={'request': request}).data,
      'recent': CoursesSerializer(qs[:limit], context={'request': request}, many=True).data
    }
    return data