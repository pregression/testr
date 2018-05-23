from django.test import TestCase
from django.urls import reverse


class LandingPageViewTestCase(TestCase):
    def test_200_response(self):
        response = self.client.get(reverse('marketing_home'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'marketing/index.html')


class NewSubscriptionViewTestCase(TestCase):
    pass
