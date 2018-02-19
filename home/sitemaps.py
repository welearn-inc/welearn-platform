from django.contrib import sitemaps
from django.core.urlresolvers import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'
    
    def items(self):
        return ['home','robots','humans','google_verify','terms','privacy',]
    
    def location(self, item):
        return reverse(item)