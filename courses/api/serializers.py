from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from courses.models import Course

class CoursesSerializer(serializers.ModelSerializer):
  # uri = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = Course
    fields = [
     'id','source','name','slug','headline','category','image_url',
     'lectures','duration',
     'price','language','level','rating',
     'created_date', 'modified_date',
     'featured','active',
     'instructor',
     'url'
    ]

  # def get_uri(self, obj):
  #   request = self.context.get('request')
  #   return api_reverse('api-courses:detail', kwargs={"slug": obj.slug}, request=request)