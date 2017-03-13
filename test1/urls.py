# -*- coding: utf-8 -*-
from django.conf.urls import url,patterns

urlpatterns = patterns(
    'test1.views',
    url(r'^$','index'),
    url(r'^(?P<test_id>[0-9]+)/(?P<api_id>[0-9]+)/$','sss'),
)