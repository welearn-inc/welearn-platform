from django.conf.urls import url

# from courses.views import courses
# from courses.views import enrollment
# from courses.views import teaching

from courses.views import courses

urlpatterns = [
    url(r'^courses/$', courses.course_list, name='course-list'),
    url(r'^courses/create/$', courses.course_create, name='course-create'),
    url(r'^courses/create-module/$', courses.module_create, name='module-create'),
    url(r'^courses/(?P<slug>[\w-]+)/$', courses.course_detail, name='course-detail'),
    url(r'^courses/(?P<slug>[\w-]+)/edit/$', courses.course_update, name='course-update'),
    url(r'^courses/(?P<slug>[\w-]+)/delete/$', courses.course_delete, name='course-delete'),
    # url(r'^courses/test/$', courses.some_view),
    
    # url(r'^courses/(?P<slug>[\w-]+)/(?P<lslug>[\w-]+)/$', ModuleDetailView.as_view(), name='module-detail'),

    # url(r'^courses/(?P<slug>[\w-]+)/enroll/$', CourseEnrollView.as_view(), name='enroll'),
    # url(r'^courses/(?P<slug>[\w-]+)/disenroll/$', CourseDisenrollView.as_view(), name='disenroll'),

#     # Enrollment(s)
#     url(r'^enrollment$', enrollment.enrollment_page),
#     url(r'^disenroll', enrollment.disenroll),
         
#     # Teaching
#     url(r'^teaching$', teaching.teaching_page),
                       
#     url(r'^save_course$', teaching.save_course),
#     url(r'^course_delete$', teaching.course_delete),
] 