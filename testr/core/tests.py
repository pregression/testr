# from django.test import TestCase
from unittest import TestCase


class DummyTestCase(TestCase):
    def test_test(self):
        self.assertTrue(True)
