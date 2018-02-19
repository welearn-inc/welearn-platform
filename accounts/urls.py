from django.conf import settings
from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth.views import logout

from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    url(r'^profile/$',
        TemplateView.as_view(template_name="profile.html"),
        name='profile'),

    url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    url(r'^email-verification/$',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),

    url(r'^login/$', TemplateView.as_view(template_name="login.html"),
        name='login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
        name='logout'),

    url(r'^password-reset/$',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    url(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),
    url(r'^password-change/$',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),
    # this url is used to generate email content
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),

    # REST Auth endpoints
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # url(r'^account/', include('allauth.urls')),
    # url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
]

from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)

urlpatterns += [
    url(
        r'^socialaccounts/$',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    url(
        r'^socialaccounts/(?P<pk>\d+)/disconnect/$',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    )
]