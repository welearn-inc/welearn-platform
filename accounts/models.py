from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
  user = models.ForeignKey(User)
    
  def __str__(self):
    return self.user.username

  @property
  def student_id(self):
    return self.id

  @property
  def fullname(self):
    return self.user.first_name + " " + \
      self.user.last_name + " "

class Teacher(models.Model):
  user = models.ForeignKey(User)
    
  def __str__(self):
    return self.user.username

  @property
  def teacher_id(self):
    return self.id

  @property
  def fullname(self):
    return self.user.first_name + " " + \
      self.user.last_name + " "
