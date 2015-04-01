#!/usr/bin/python
#encoding=utf-8


from django.conf.urls import include, url
from django.contrib import admin
from sellfruit.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'sellfruit_wecharweb_python.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^order/$',order),
    url(r'^comment/$',comment),
]
