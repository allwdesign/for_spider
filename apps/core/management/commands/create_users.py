from django.core.management.base import BaseCommand
from django.utils import timezone

from account.models import User


class Command(BaseCommand):
	help = 'Create 10 users'

	def handle(self, *args, **options):
		names = ['Test' + str(i) for i in range(1,11)]

		for name in names:

			password = f'{name}pass'
			email = f'{name}@test.com'

			User.objects.create_user(
				username=name,
				password=password,
				email=email,
			)
			self.stdout.write(f'User {name} created successfully!')