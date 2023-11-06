from unittest import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User

class CreateSuperuserTestCase(TestCase):
    def test_create_superuser(self):
        """ Тест функции создания superuser """

        if not User.objects.filter(username='admin').exists():

            User.objects.create_superuser(username='admin', email='admin@admin.com', password='123456')

        superuser = User.objects.get(username='admin')
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
