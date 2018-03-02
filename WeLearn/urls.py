from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'', include('home.urls'), name='home'),
    url(r'', include('accounts.urls'), name='accounts'),
    url(r'', include('courses.urls'), name='courses'),

    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/auth/', include('accounts.api.urls', namespace='api-auth')),
    url(r'^api/user/', include('accounts.api.user.urls', namespace='api-user')),
    url(r'^api/courses/', include('courses.api.urls', namespace='api-courses'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
