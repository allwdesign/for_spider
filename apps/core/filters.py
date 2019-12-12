# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters

from core.models import Organization


class OrganizationFilter(filters.FilterSet):
	min_price = filters.NumberFilter(field_name='service__price', lookup_expr='gte')
	max_price = filters.NumberFilter(field_name='service__price', lookup_expr='lte')
	category = filters.CharFilter(field_name='service__category', lookup_expr='iexact')

	class Meta:
		model = Organization
		fields = ('category', 'min_price', 'max_price')