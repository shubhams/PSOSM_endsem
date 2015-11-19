from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'endsem.views.home', name='home'),
    url(r'^final/', include('final.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
