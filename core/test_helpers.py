from django.test import TestCase

from core.models import User


class AuthenticatedTestCase(TestCase):
    def setUp(self):
        self.email = "foo@bar.com"
        self.password = "bar"
        self.user = User.objects.create_user(self.email, self.password)
        logged_in = self.client.login(email=self.user.email, password=self.password)
        self.assertTrue(logged_in)
