from django.contrib.auth.models import User

from rest_framework import views, generics, mixins, permissions
from rest_framework.response import Response

from courses.models import Course

from .serializers import CoursesSerializer

class CoursesAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  queryset           = Course.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  serializer_class   = CoursesSerializer
  search_fields      = ('name', 'headline', 'category')
  ordering_fields    = ('source', 'timestamp')
  
  def get_queryset(self):
    query = self.request.GET.get("q")
    if query:
        qs = Course.objects.search(query)
    else:
        qs = Course.objects.all()
    return qs

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  def post_save(self, course, *args, **kwargs):
    if type(course.tags) is list:
        # If tags were provided in the request
        saved_course= Course.objects.get(slug=course.slug)
        for tag in course.tags:
            saved_course.tags.add(tag)

class CoursesAPIDetailView(
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  generics.RetrieveAPIView):
  permission_classes    = [permissions.IsAdminUser] 
  serializer_class      = CoursesSerializer
  lookup_field          = 'slug'

  def get_serializer_context(self):
    return {'request': self.request}

  def get_queryset(self):
    return Course.objects.all()

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def patch(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)