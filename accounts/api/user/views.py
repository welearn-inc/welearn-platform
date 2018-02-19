from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.response import Response

from courses.api.serializers import CoursesSerializer
from courses.api.views import CoursesAPIView
from courses.models import Course

from .serializers import UserDetailSerializer

User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
  serializer_class    = UserDetailSerializer
  lookup_field        = 'username'

  def get_serializer_context(self):
    return {'request': self.request}

  def get_queryset(self):
    return User.objects.filter(is_active=True)

class UserCoursesAPIView(CoursesAPIView):
    serializer_class = CoursesSerializer
    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Course.objects.none()
        return Course.objects.filter(user__username=username)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)