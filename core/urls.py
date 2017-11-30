# -*- coding: utf-8 -*-
"""Specifies the URL schemes for the application core"""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^organizations/(?P<district_id>[0-9]+)/$',
        views.OrganizationList.as_view(),
        name='organization-list'),
    url(r'^organization/(?P<pk>[0-9]+)/$',
        views.OrganizationDetail.as_view(),
        name='organization-detail'),
    url(r'^services/(?P<pk>[0-9]+)/$', views.ServiceDetail.as_view(),
        name='service-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
