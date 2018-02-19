from django.test import TestCase

from django.contrib.auth import get_user_model

from .models import Course
User = get_user_model()

class CoursesTestCase(TestCase):
  def setUp(self):
    user = User.objects.create(username='test', email='hello@test.com')
    user.set_password("Aa111111")
    user.save()


  def test_creating_course(self):
    user = User.objects.get(username='test')
    obj = Course.objects.create(user=user, name='My Awesome Course', description='My description')
    self.assertEqual(obj.id, 1)
    qs = Course.objects.all()
    self.assertEqual(qs.count(), 1) 


