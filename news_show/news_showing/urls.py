from django.conf.urls import include, url
from django.contrib import admin
from news_show import *
urlpatterns = [
    url(r'^$'views.index),
    url(r'^news_list/$',views.index),
    url(r'^news_info/([0-9]{1,5})/$',views.info),
    url(r'^admin/', include(admin.site.urls)),
]
