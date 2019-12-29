from django.core.management.base import BaseCommand

from account.models import User


class Command(BaseCommand):
    help = 'Delete all users, exclude superuser'

    def handle(self, *args, **kwargs):


        for user in User.objects.filter(is_superuser=False):
            try:
                id = user.pk

                user.delete()

                self.stdout.write(f'The user {user.username} ({id}) is deleted!')

            except User.DoesNotExist:

                self.stdout.write(f'The user with id {id} does not exist.')