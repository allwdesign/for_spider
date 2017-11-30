# -*- coding: utf-8 -*-
# NOTE: render imported but not used
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# NOTE: renderers imported but not used
from rest_framework import generics, renderers
# NOTE: Response imported but not used
from rest_framework.response import Response
# NOTE: better way to import is
# from core import models
# ...
# models.Organization.objects.all()
# NOTE: District and Category imported but not used
from .models import District, Category, Service, Organization
# NOTE: import Error module serializer does not have OrganizationDetailSerializer
from .serializers import OrganizationSerializer, OrganizationDetailSerializer, ServiceSerializer
# NOTE: import Error - import module to itself !!!
from core import views


class OrganizationList(generics.ListAPIView):
    """Display all Organizations by district"""
    serializer_class = OrganizationSerializer
    # NOTE: Reason to use FitlerBackend if all filtering goes through get_queryset method?
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('=organization_name', '=services__service_name')

    def get_queryset(self):
        district = self.kwargs['district_id']
        
        # NOTE: not the best way to do this. Try to user lookup params
        queryset = Organization.objects.filter(districts=district)

        category = self.request.query_params.get('category', None)

        # Filtering by max price http://localhost:8000/organizations/5/?max_price=500.0
        max_price = self.request.query_params.get('max_price', None)

        # Filtering by min price http://localhost:8000/organizations/1/?min_price=280.0
        min_price = self.request.query_params.get('min_price', None)

        if category is not None:
            # Filter by service category in this organization with set district
            # http://localhost:8000/organizations/4/?category=appliances
            # NOTE:
            # category_name__iexact - search by exact string, not filtering
            # filtering more like
            # .fitler(services__category_id=cateogry_id)
            # or
            # .filter(service__category=category) (if category is an instance of Category model)
            return queryset.filter(services__category__category_name__iexact=category)

        # NOTE: what if incoming values of max_price of min_price are not an integers?
        if (min_price and max_price) is not None:
            # Get the price between min_price and max_price values
            queryset = queryset.filter(services__price__range=(min_price, max_price))

        elif min_price is not None:
            # Get everything that is greater or equal to this price
            queryset = queryset.filter(services__price__gte=min_price)

        elif max_price is not None:
            # Get everything that is less or equal to this price
            queryset = queryset.filter(services__price__lte=max_price)
        
        # NOTE: next row also returns queryset so this `else` block useless
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
    
 # NOTE: also project/settings.py missing, same as core/migrations folder
