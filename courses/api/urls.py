from django.conf.urls import url

from .views import CoursesAPIView, CoursesAPIDetailView

urlpatterns = [
    url(r'^$', CoursesAPIView.as_view(), name='list'),
    url(r'^(?P<slug>.*)/$', CoursesAPIDetailView.as_view(), name='detail')
]
 