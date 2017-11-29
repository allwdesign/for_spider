# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from core.views import OrganizationViewSet


router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewSet)

urlpatterns = router.urls
