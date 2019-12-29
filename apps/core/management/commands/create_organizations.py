import random
import itertools

from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import District, Service, Organization


class Command(BaseCommand):
	help = (
		f'Create 10 organizations. Districts and services should already '
		f'be created with the help of command managers')

	@staticmethod
	def create_list_with_random_combinations_of_indexes(queryset, n=3):
		"""
		Сreates the list of unique tuples of indices that are not out of range
		for objects.
		Combinations of indexes have a random size.
		"""
		indexes = itertools.combinations([num for num in range(len(queryset))], n)
		tupple_random_sizes = lambda x: x[:random.choice(range(len(queryset)))]
		# return list of tuples (without empty tuples)
		return list(set(t for t in map(tupple_random_sizes, indexes) if t))

	def handle(self, *args, **options):
		organizations = [
			'Ltd MediasCo',
			'Ltd Unipix',
			'TechCo',
			'Test Staff Org',
			'MisterBoo',
			'CoolIceCream',
			'LTD Beter Way',
			'Ltd HoneyCorp',
			'Billy Cars rent',
			'Ltd StarsGame',]

		# five types of services
		services = Service.objects.all()
		s_indexes = self.create_list_with_random_combinations_of_indexes(services)

		districts = District.objects.all()
		d_indexes = self.create_list_with_random_combinations_of_indexes(districts)

		for name in organizations:
			description = f'Something about {name}'

			org = Organization.objects.create(
				organization_name=name,
				description=description,
			)

			# Associate the Organization with a Service and a Districts
			for i in random.choice(s_indexes):
				org.services.add(services[i])

			for i in random.choice(d_indexes):
				org.districts.add(districts[i])

			self.stdout.write(f'Organization {name} created successfully!')

