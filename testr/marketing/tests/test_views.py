from django.test import TestCase


class LandingPageViewTestCase(TestCase):
    def test_200_response(self):
        response = self.client.get('')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'marketing/index.html')


class NewSubscriptionViewTestCase(TestCase):
    pass
