# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import generics, renderers
from rest_framework.response import Response
from .models import District, Category, Service, Organization
from .serializers import OrganizationSerializer, ServiceSerializer
from core import views

class OrganizationList(generics.ListCreateAPIView):
    """Display all Organizations by district"""
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        district = self.kwargs['district_id']
        return Organization.objects.filter(districts=district)



class ServiceDetail(generics.RetrieveUpdateAPIView):
    """Display current service"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
