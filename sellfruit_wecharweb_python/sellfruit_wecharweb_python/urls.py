#!/usr/bin/python
#encoding=utf-8


from django.conf.urls import include, url
from django.contrib import admin
from sellfruit.views import *
from sellfruit.manage import orderForm
from sellfruit.queryorder import queryorder

from canteen_menu.views import canteenmenu

from activity.views import wuerling,wuerling_action

from graduate_flower.views import graduate_flower, graduate_flower_action, order_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'sellfruit_wecharweb_python.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^order/$',order),
    url(r'^comment/(\S)+/$',comment),
    url(r'^tocomment/$',toComment),
    url(r'^manage/$', orderForm),
    url(r'^queryorder/$', queryorder),

    #canteen_menu食堂菜单
    url(r'^canteenmenu/$', canteenmenu),

    #activity活动app
    url(r'^wuerling/$', wuerling),
    url(r'^wuerlingaction/$',wuerling_action),

    #毕业季买花
    url(r'^graduate/flower/$', graduate_flower),
    url(r'^graduate/flower/action/$', graduate_flower_action),
    url(r'^graduate/flower/orderview/$', order_view),

]
