import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import APIException

from core.models import District, Category, Service, Organization
from core.serializers import (
    OrganizationSerializer,
    OrganizationDetailSerializer,
    ServiceSerializer,
)

class OrganizationListViewTest(APITestCase):
	def setUp(self):
		"""Create district, category, service, organization"""
		self.district_1 = District.objects.create(
			district_name='UMR')
		self.district_2 = District.objects.create(
			district_name='KMR')
		self.district_1.save()
		self.district_1.save()

		self.category_eat = Category.objects.create(category_name='Eat')
		self.category_eat.save()

		self.service_delivery_eat = Service.objects.create(
			service_name='Delivery eat',
			category=self.category_eat,
			price=700,
		)
		self.service_delivery_eat.save()
		self.org_1 = Organization.objects.create(
			organization_name='Ltd Mister Bo',
			description='Something about Mister Bo',
		)
		self.org_1.save()
		self.org_1.districts.add(self.district_1, self.district_2)
		self.org_1.services.add(self.service_delivery_eat)

		self.org_2 = Organization.objects.create(
			organization_name='Ltd Unipix',
			description='Something about Ltd Unipix',
		)
		self.org_2.save()
		self.org_2.districts.add(self.district_1)
		self.org_2.services.add(self.service_delivery_eat)

	def test_get_all_objects_filter_by_district(self):
		"""
		Ensure we can get all organizations objects in that district.
		"""
		data = [
			{
				'id': 1,
				'organization_name': 'Ltd Mister Bo',
				'description': 'Something about Mister Bo',
				'districts': [2, 1],
				'services': [1,],
			},
			{
				'id': 2,
				'organization_name': 'Ltd Unipix',
				'description': 'Something about Ltd Unipix',
				'districts': [1,],
				'services': [1,],
			},
		]
		url = reverse(
			'core:organization-list',
			kwargs={'district_id':self.district_1.pk})
		response = self.client.get(url, format='json')

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.json(), data)
		self.assertEqual(len(response.data), 2)