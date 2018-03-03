from django.test import TestCase

class LicenseViewTestCase(TestCase):
    def test_200_response(self):
        response = self.client.get('/license/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'core/license.html')

    def test_redirect_without_trailing_slash(self):
        response = self.client.get('/license')
        self.assertRedirects(response, '/license/', 301)


class TermsViewTestCase(TestCase):
    def test_200_response(self):
        response = self.client.get('/terms/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'core/terms.html')

    def test_redirect_without_trailing_slash(self):
        response = self.client.get('/terms')
        self.assertRedirects(response, '/terms/', 301)

class PrivacyViewTestCase(TestCase):
    def test_200_response(self):
        response = self.client.get('/privacy/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'core/privacy.html')

    def test_redirect_without_trailing_slash(self):
        response = self.client.get('/privacy')
        self.assertRedirects(response, '/privacy/', 301)
