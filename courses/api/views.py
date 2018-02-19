from django.contrib.auth.models import User

from rest_framework import generics, mixins, permissions

from accounts.api.permissions import IsOwnerOrReadOnly
from courses.models import Course
from .serializers import CoursesSerializer

class CoursesAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  serializer_class   = CoursesSerializer
  search_fields      = ('user__username', 'name')
  ordering_fields    = ('user', 'timestamp')

  def get_queryset(self):
    return Course.objects.all()
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class CoursesAPIDetailView(
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  generics.RetrieveAPIView):
  permission_classes    = [IsOwnerOrReadOnly] 
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