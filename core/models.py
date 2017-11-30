# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class District(models.Model):
    """District model"""
    district_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"

    def __str__(self):
        return self.district_name


class Category(models.Model):
    """Category model"""
    category_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class Service(models.Model):
    """Service model"""
    service_name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, related_name='categories')
    price = models.DecimalField(decimal_places=2, max_digits=20)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.service_name


class Organization(models.Model):
    """Organization model"""
    organization_name = models.CharField(max_length=250)
    description = models.TextField()
    districts = models.ManyToManyField(District)
    services = models.ManyToManyField(Service)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return '%s %s' % (self.organization_name, self.description)