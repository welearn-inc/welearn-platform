from django.contrib.auth.models import User

from rest_framework import views, generics, mixins, permissions
from rest_framework.response import Response

from accounts.models import Student
from accounts.models import Teacher
from courses.models import Course

from .serializers import CoursesSerializer
from accounts.api.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly

class CoursesAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  queryset           = Course.objects.all()
  permission_classes = [IsAdminOrReadOnly]
  serializer_class   = CoursesSerializer
  search_fields      = ('user__username', 'name')
  ordering_fields    = ('user', 'timestamp')
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  def perform_create(self, serializer):
    try:
      teacher = Teacher.objects.get(user=self.request.user)
    except Teacher.DoesNotExist:
       teacher = Teacher.objects.create(user=self.request.user)
    serializer.save(user=self.request.user, teacher=teacher)

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

class CoursesEnrollView(views.APIView):
  def post(self, request, slug, format=None):
    course = get_object_or_404(Course, slug=slug)
    student = Student.objects.get(user=request.user)
    try:
      Course.objects.get(
          slug=slug,
          students__student_id=student.student_id
      )
    except Course.DoesNotExist:
        course.students.add(student)
    return Response({'status' : 'success', 'message' : 'enrolled' })