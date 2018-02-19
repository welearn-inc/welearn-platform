from django.conf.urls import url, include

from .views import UserDetailAPIView
from .views import UserCoursesAPIView

urlpatterns = [
    url(r'^(?P<username>\w+)/$', UserDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<username>\w+)/courses/$', UserCoursesAPIView.as_view(), name='courses-list'),
]
