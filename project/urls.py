# -*- coding: utf-8 -*-
"""project URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
]

# A pattern to include the login and logout views for the browsable API.
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]