# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, renderers
from rest_framework.response import Response
from .models import District, Category, Service, Organization
from .serializers import OrganizationSerializer, OrganizationDetailSerializer, ServiceSerializer
from core import views


class OrganizationList(generics.ListAPIView):
    """Display all Organizations by district"""
    serializer_class = OrganizationSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('=organization_name', '=services__service_name')

    def get_queryset(self):
        district = self.kwargs['district_id']

        queryset = Organization.objects.filter(districts=district)

        category = self.request.query_params.get('category', None)

        # Filtering by max price http://localhost:8000/organizations/5/?max_price=500.0
        max_price = self.request.query_params.get('max_price', None)

        # Filtering by min price http://localhost:8000/organizations/1/?min_price=280.0
        min_price = self.request.query_params.get('min_price', None)

        if category is not None:
            # Filter by service category in this organization with set district
            # http://localhost:8000/organizations/4/?category=appliances
            return queryset.filter(services__category__category_name__iexact=category)

        if (min_price and max_price) is not None:
            # Get the price between min_price and max_price values
            queryset = queryset.filter(services__price__range=(min_price, max_price))

        elif min_price is not None:
            # Get everything that is greater or equal to this price
            queryset = queryset.filter(services__price__gte=min_price)

        elif max_price is not None:
            # Get everything that is less or equal to this price
            queryset = queryset.filter(services__price__lte=max_price)

        else:
            return queryset

        return queryset


class OrganizationDetail(generics.RetrieveAPIView):
    """Display current Organization"""
    queryset = Organization.objects.all()
    serializer_class = OrganizationDetailSerializer


class ServiceDetail(generics.RetrieveAPIView):
    """Display current service"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
