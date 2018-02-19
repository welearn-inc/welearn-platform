from django.conf.urls import url

from home.views import home
from home.views import txt
from home.views import privacy
from home.views import terms
from home.views import google

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # Home
    url(r'^$', home.home_page, name='home'),

    # Pages
    url(r'^terms$', terms.terms_page, name='terms'),
    url(r'^privacy', privacy.privacy_page, name='privacy'),

    # Other Pages
    url(r'^robots\.txt$', txt.robots_txt_page, name='robots'),
    url(r'^credits\.txt$', txt.humans_txt_page, name='credits'),
                       
    # Google Verify
    url(r'^google$', google.google_verify_page, name='google_verify'),                       
                       
    # Sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap')
]