from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save

from taggit.managers import TaggableManager

from courses.utils import unique_slug_generator
from accounts.models import Student
from accounts.models import Teacher

COURSE_CATEGORY_TYPES = (
    ('Aeronautics & Astronautics', 'Aeronautics & Astronautics'),
    ('Anesthesia', 'Anesthesia'),
    ('Anthropology', 'Anthropology'),
    ('Applied Physics', 'Applied Physics'),
    ('Art or Art History', 'Art & Art History'),
    ('Astrophysics', 'Astrophysics'),
    ('Biochemistry', 'Biochemistry'),
    ('Bioengineering', 'Bioengineering'),
    ('Biology', 'Biology'),
    ('Business', 'Business'),
    ('Cardiothoracic Surgery', 'Cardiothoracic Surgery'),
    ('Chemical and Systems Biology', 'Chemical and Systems Biology'),
    ('Chemical Engineering', 'Chemical Engineering'),
    ('Chemistry', 'Chemistry'),
    ('Civil and Environmental Engineering', 'Civil and Environmental Engineering'),
    ('Classics', 'Classics'),
    ('Communication', 'Communication'),
    ('Comparative Literature', 'Comparative Literature'),
    ('Comparative Medicine', 'Comparative Medicine'),
    ('Computer Science', 'Computer Science'),
    ('Dermatology', 'Dermatology'),
    ('Developmental Biology', 'Developmental Biology'),
    ('East Asian Languages and Cultures', 'East Asian Languages and Cultures'),
    ('Economics', 'Economics'),
    ('Education', 'Education'),
    ('Electrical Engineering', 'Electrical Engineering'),
    ('English', 'English'),
    ('French', 'French'),
    ('Genetics', 'Genetics'),
    ('General Eduction', 'General Education'),
    ('Geological and Environmental Sciences', 'Geological and Environmental Sciences'),
    ('Geophysics', 'Geophysics'),
    ('Health', 'Health'),
    ('History', 'History'),
    ('Latin American Cultures', 'Latin American Cultures'),
    ('Law School', 'Law School'),
    ('Linguistics', 'Linguistics'),
    ('Management', 'Management'),
    ('Materials Science', 'Materials Science'),
    ('Mathematics', 'Mathematics'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Medicine', 'Medicine'),
    ('Microbiology and Immunology', 'Microbiology and Immunology'),
    ('Molecular and Cellular Physiology', 'Molecular and Cellular Physiology'),
    ('Music', 'Music'),
    ('Neurobiology', 'Neurobiology'),
    ('Neurology', 'Neurology'),
    ('Neurosurgery', 'Neurosurgery'),
    ('Obstetrics and Gynecology', 'Obstetrics and Gynecology'),
    ('Ophthalmology', 'Ophthalmology'),
    ('Orthopaedic Surgery', 'Orthopaedic Surgery'),
    ('Otolaryngology', 'Otolaryngology'),
    ('Pathology', 'Pathology'),
    ('Pediatrics', 'Pediatrics'),
    ('Philosophy', 'Philosophy'),
    ('Physics', 'Physics'),
    ('Political Science', 'Political Science'),
    ('Psychiatry', 'Psychiatry'),
    ('Psychology', 'Psychology'),
    ('Radiation Oncology', 'Radiation Oncology'),
    ('Radiology', 'Radiology'),
    ('Religious Studies', 'Religious Studies'),
    ('Slavic Languages and Literature', 'Slavic Languages and Literature'),
    ('Sociology', 'Sociology'),
    ('Statistics', 'Statistics'),
    ('Surgery', 'Surgery'),
    ('Theater and Performance Studies', 'Theater and Performance Studies'),
    ('Other', 'Other')
)

# class CourseQuerySet(models.query.QuerySet):
#   def active(self):
#     return self.filter(active=True)

#   def featured(self):
#     return self.filter(featured=True)

  # def search(self, query):
  #   return self.filter(
  #     Q(name__icontains=query) or
  #     Q(slug__icontains=query) or
  #     Q(embed_icontains=query)
  #   )

# class CourseManager(models.Manager):
#   def get_queryset(self):
#     return CourseQuerySet(self.model, using=self._db)

#   def all(self):
#     return self.get_queryset().active()

#   def featured(self):
#     return self.get_queryset().featured().active() 

  # def search(self, query):
  #   return self.get_queryset().search(query).active()

def upload_courses_media(instance, filename):
  return "courses/{slug}/{filename}".format(slug=instance.slug, filename=filename)

class Course(models.Model):
  # CHOICES
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

  name            = models.CharField(max_length=50)
  slug            = models.SlugField(unique=True, blank=True)
  user            = models.ForeignKey(settings.AUTH_USER_MODEL)
  
  headline        = models.CharField(max_length=100, null=True)
  description     = models.TextField(null=True)
  category        = models.CharField(max_length=140, choices=COURSE_CATEGORY_TYPES, default='Personal Development')
  image           = models.ImageField(upload_to=upload_courses_media, blank=True, null=True)
  video           = models.ImageField(upload_to=upload_courses_media, blank=True, null=True)

  goals           = models.TextField(null=True)
  benefits        = models.TextField(null=True)

  pricing         = models.CharField(max_length=6, choices=COURSE_PRICING_CHOICES, default='$ FREE') 
  language        = models.CharField(max_length=10, choices=COURSE_LANGUAGES_CHOICES, default='English')
  level           = models.CharField(max_length=12, choices=COURSE_LEVEL_CHOICES, default='Beginner')

  created_date    = models.DateField(auto_now_add=True)
  modified_date   = models.DateField(auto_now=True)

  featured        = models.BooleanField(default=False)
  active          = models.BooleanField(default=True)

  students        = models.ManyToManyField(Student)
  teacher         = models.ForeignKey(Teacher, related_name='courses')

  tags = TaggableManager()


  def __str__(self):
    return self.name

  @property
  def course_id(self):
     return self.id

  @property
  def title(self):
    return self.name

class Module(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL)
    name            = models.CharField(max_length=50, null=True)
    description     = models.TextField(null=True)
    media_url       = models.URLField(null=True)
    body_text       = models.TextField(blank=True, null=True)
    course          = models.ForeignKey(Course, related_name='modules')

    created_date    = models.DateField(auto_now_add=True)
    modified_date   = models.DateField(auto_now=True)


def course_pre_save_receiver(sender, instance, *args, **kwargs):
  if not instance.slug:
    instance.slug = unique_slug_generator(instance)

pre_save.connect(course_pre_save_receiver, sender=Course)
