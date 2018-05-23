from django.test import TestCase
from django.urls import reverse
from json import dumps

class LicenseViewTestCase(TestCase):
    def test_200_response(self):
        response = self.client.get(reverse('license'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'core/license.html')


class TermsViewTestCase(TestCase):
    def test_200_response(self):
        response = self.client.get(reverse('terms'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'core/terms.html')


class PrivacyViewTestCase(TestCase):
    def test_200_response(self):
        response = self.client.get(reverse('privacy'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'core/privacy.html')


class ReportCspViewTestCase(TestCase):
    def test_get_response(self):
        response = self.client.get(reverse('report_csp'))
        self.assertEquals(204, response.status_code)

    def test_post_response(self):
        response = self.client.post(
            reverse('report_csp'),
            dumps({"foo":"bar"}),
            content_type='application/json')
        self.assertEquals(200, response.status_code)
