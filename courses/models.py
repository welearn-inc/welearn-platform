from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save

from taggit.managers import TaggableManager

from courses.utils import unique_slug_generator

class CourseQuerySet(models.query.QuerySet):
  def active(self):
    return self.filter(active=True)

  def featured(self):
    return self.filter(featured=True)

  def search(self, query):
    return self.filter(
      Q(name__icontains=query) or
      Q(headline_icontains=query) or
      Q(category__icontains=query)
    )

class CourseManager(models.Manager):
  def get_queryset(self):
    return CourseQuerySet(self.model, using=self._db)

  def all(self):
    return self.get_queryset().active()

  def featured(self):
    return self.get_queryset().featured().active() 

  def search(self, query):
    return self.get_queryset().search(query).active()

class Course(models.Model):
  COURSE_PRICING_CHOICES = (
      ('$ FREE', '$ FREE'),
      ('29$',  '29$'),
      ('59$',  '59$'),
      ('79$',  '79$'),
      ('99$',  '99$'),
    )
  COURSE_LANGUAGES_CHOICES = (
      ('English', 'English'),
      ('Spanish', 'Spanish'),
      ('Chinese', 'Chinese'),
      ('Hindi', 'Hindi'),
      ('Arabic', 'Arabic'),  
      ('German', 'German'),
      ('French', 'French'),
      ('Italian', 'Italian'),    
      ('Russian', 'Russian'), 
      ('Portuguese', 'Portuguese'),
      ('Japanese', 'Japanese'), 
    )
  COURSE_LEVEL_CHOICES = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
  )

  source          = models.CharField(max_length=20, null=True)
  
  name            = models.CharField(max_length=100)
  slug            = models.SlugField(max_length=255, unique=True, blank=True)
  
  headline        = models.CharField(max_length=255, null=True)
  category        = models.CharField(max_length=140, default='Personal Development')
  image_url       = models.TextField(null=True)

  lectures        = models.CharField(max_length=10, null=True)
  duration        = models.CharField(max_length=10, null=True) 

  language        = models.CharField(max_length=10, choices=COURSE_LANGUAGES_CHOICES, default='English')
  rating          = models.CharField(max_length=10, null=True) 
  level           = models.CharField(max_length=12, choices=COURSE_LEVEL_CHOICES, default='Beginner')
  price           = models.CharField(max_length=10, choices=COURSE_PRICING_CHOICES, default='$ FREE') 

  url             = models.TextField(null=True)
  
  created_date    = models.DateField(auto_now_add=True)
  modified_date   = models.DateField(auto_now=True)

  featured        = models.BooleanField(default=False)
  active          = models.BooleanField(default=True)

  instructor      = models.CharField(max_length=100, null=True)

  tags            = TaggableManager()
  objects 		  = CourseManager()

  def __str__(self):
    return self.name

  @property
  def course_id(self):
     return self.id

  @property
  def title(self):
    return self.name

def course_pre_save_receiver(sender, instance, *args, **kwargs):
  if not instance.slug:
    instance.slug = unique_slug_generator(instance)

pre_save.connect(course_pre_save_receiver, sender=Course)
