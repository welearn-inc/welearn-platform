from django.contrib import admin

from .models import Course

class CoursesAdmin(admin.ModelAdmin):
  list_display = ['user', '__str__', 'image']
  class Meta:
    model = Course

admin.site.register(Course)