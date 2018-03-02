from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.conf import settings
from courses.models import Course

class Command(BaseCommand):
  def handle(self, *args, **options):
    Course.objects.all().delete()
    Course.objects.create(
        id=1,
        name="Super Affiliate",
        headline="TEST HEADLINE",
        description="MY TEST description",
        image="loading.gif",
        user=User.objects.first()
    )
