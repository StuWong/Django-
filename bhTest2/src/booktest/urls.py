
from django.conf.urls import url,include
from booktest.views import *
urlpatterns = [
    url(r'^$',index),
    url(r'^area',area),
    url(r'^pro/(\d+)$',pro),
    url(r'^city/(\d+)$',city),
    url(r'^dis/(\d+)$',dis),
]
