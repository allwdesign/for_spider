# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .models import District, Category, Service, Organization
from .serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """Organization viewset that provides the standart actions"""
    """
    Work only in shell!
    district = District.objects.get(id=pk)

    queryset = district.organization_set.all()
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
