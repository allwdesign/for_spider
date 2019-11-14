# -*- coding: utf-8 -*-
"""Specifies the URL schemes for the application core"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import (
	OrganizationList,
	OrganizationDetail,
	ServiceDetail,
)


urlpatterns = [
    path('organizations/(<int:district_id>/',
        views.OrganizationList.as_view(),
        name='organization-list'),
    path('organization/(<int:pk>/',
        views.OrganizationDetail.as_view(),
        name='organization-detail'),
    path('services/<int:pk>/', views.ServiceDetail.as_view(),
        name='service-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
