# -*- coding: utf-8 -*-
"""Specifies the URL schemes for the application core"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import (
	OrganizationList,
	OrganizationDetail,
	ServiceDetail,
)

app_name = 'core'

urlpatterns = [
	path('organizations/(<int:district_id>/',
		OrganizationList.as_view(),
		name='organization-list'),
	path('organization/(<int:pk>/',
		OrganizationDetail.as_view(),
		name='organization-detail'),
	path('services/<int:pk>/', ServiceDetail.as_view(),
		name='service-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
