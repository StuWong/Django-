"""bhTest01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from booktest.views import *
urlpatterns = [
    url(r'^$', index),
    #正则中加上括号，在view中的函数就可以获取到。
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)',detail),
    url(r'^(\d+)',show),
    url(r'^getTest1$',getTest1),
    url(r'^getTest2$',getTest2),
    url(r'^getTest3$',getTest3),
    url(r'^postTest1',postTest1),
    url(r'^postTest2$',postTest2),
    url(r'^cookieTest$',cookieTest),
    url(r'^redTest$',redTest),
    url(r'^session1$',session1),
    url(r'^session2$',session2),
     url(r'^session3$',session3),
    url(r'^sessionHandle$',sessionHandle)
]
