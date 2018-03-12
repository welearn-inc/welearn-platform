from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls import handler404, handler500
from django.http import JsonResponse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^courses/', include('courses.api.urls', namespace='api-courses'))
] 

def response404(request, status=404, message='Requested endpoint not found', data=None):
    data = {'status': status, 'message': message}
    return JsonResponse(data=data, status=status)

def response500(request, status=500, message='Internal Server Error', data=None):
    data = {'status': status, 'message': message}
    return JsonResponse(data=data, status=status)

handler404 = response404
handler500 = response500