# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from core.views import OrganizationViewSet, ServiceViewSet


router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = router.urls
