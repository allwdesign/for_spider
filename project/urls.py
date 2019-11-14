# -*- coding: utf-8 -*-
"""project URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls',)),
]

# A pattern to include the login and logout views for the browsable API.
urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')
]
