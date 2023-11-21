from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            username='admin',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123456')
        user.save()