# -*- coding: utf-8 -*-
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, renderers
from rest_framework.response import Response
from .models import District, Category, Service, Organization
from .serializers import OrganizationSerializer, ServiceSerializer
from core import views


class OrganizationList(generics.ListCreateAPIView):
    """Display all Organizations by district"""
    serializer_class = OrganizationSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        district = self.kwargs['district_id']
        queryset = Organization.objects.filter(districts=district)

        # filtering by max price http://localhost:8000/organizations/5/?max_price=500.0
        max_price = self.request.query_params.get('max_price', None)

        # filtering by min price http://localhost:8000/organizations/1/?min_price=280.0
        min_price = self.request.query_params.get('min_price', None)

        if max_price is not None:
            queryset = queryset.filter(services__price__lte=max_price)

        if min_price is not None:
            queryset = queryset.filter(services__price__gte=min_price)

        return queryset


class ServiceDetail(generics.RetrieveUpdateAPIView):
    """Display current service"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
