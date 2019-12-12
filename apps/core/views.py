# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from core.filters import OrganizationFilter
from core.models import Service, Organization
from core.serializers import (
    OrganizationSerializer,
    OrganizationDetailSerializer,
    ServiceSerializer,
)


class OrganizationList(generics.ListAPIView):
    """Display all Organizations filtering by district"""
    serializer_class = OrganizationSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)  # TODO: replace into settings
    filterset_class = OrganizationFilter
    search_fields = ('=organization_name', '=services__service_name')

    def get_queryset(self):
        district = self.kwargs['district_id']
        queryset = Organization.objects.filter(districts=district)

        return queryset


class OrganizationDetail(generics.RetrieveAPIView):
    """Display current Organization"""
    queryset = Organization.objects.all()
    serializer_class = OrganizationDetailSerializer


class ServiceDetail(generics.RetrieveAPIView):
    """Display current service"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
