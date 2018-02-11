from django.test import TestCase
from django.db import IntegrityError
from testr.custom_auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User(email="foo@bar.com")
        self.user.save()

    def test_unique_email(self):
        caught = False
        try:
            u = User(email="foo@bar.com")
            u.save()
        except IntegrityError as e:
            caught = True
            self.assertTrue(len([x for x in str(e).split(' ') if x == 'duplicate']))
        finally:
            self.assertTrue(caught)

    def test_has_perm(self):
        self.assertTrue(self.user.has_perm('read'))

    def test_has_module_perms(self):
        self.assertTrue(self.user.has_module_perms('projects'))

    def test_is_staff(self):
        self.user.is_admin = True
        self.user.save()
        self.assertTrue(self.user.is_staff)

    def test_to_str(self):
        self.assertEqual(str(self.user), 'foo@bar.com')
