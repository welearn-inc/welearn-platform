from django.conf.urls import url

from .views import CoursesAPIView, CoursesAPIDetailView, CoursesEnrollView

urlpatterns = [
    url(r'^$', CoursesAPIView.as_view(), name='list'),
    url(r'^(?P<slug>.*)/enroll/$', CoursesEnrollView.as_view(), name='enroll'),
    url(r'^(?P<slug>.*)/$', CoursesAPIDetailView.as_view(), name='detail')
]
 