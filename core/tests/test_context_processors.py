from unittest import mock
from django.conf import settings
from django.test import TestCase, RequestFactory
from django.utils.timezone import now

from core.context_processors import \
    current_year,\
    established_year, \
    formatted_copyright_year, \
    app_name, \
    title_delimiter


class AbstractContextProcessorTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()


class CurrentYearTests(AbstractContextProcessorTest):
    def test_returns_dict_with_current_year_set(self):
        request = self.factory.get('/')
        data = current_year(request)
        self.assertEqual(data['current_year'], now().year)


class EstablishedYearTests(AbstractContextProcessorTest):
    def test_returns_2018(self):
        request = self.factory.get('/')
        data = established_year(request)
        self.assertEqual(data['established_year'], 2018)


class FormattedCopyRightYearTests(AbstractContextProcessorTest):
    @mock.patch('core.context_processors.__get_current_year')
    def test_displays_established_year_if_current_year_equals_established_year(self, mocked_getter):
        mocked_getter.return_value = now().year
        request = self.factory.get('/')
        data = formatted_copyright_year(request)
        self.assertEqual(data['formatted_copyright_year'], '2018')

    @mock.patch('core.context_processors.__get_current_year')
    def test_displays_dash_delimited_string_when_current_year_is_gt_established_year(self, mocked_getter):
        yr = now().year + 10
        mocked_getter.return_value = yr
        request = self.factory.get('/')
        data = formatted_copyright_year(request)
        self.assertEqual(data['formatted_copyright_year'], '2018 - %s' % yr)


class AppNameTests(AbstractContextProcessorTest):
    def test_app_name_is_read_from_settings(self):
        request = self.factory.get('/')
        data = app_name(request)
        self.assertEqual(settings.APP_NAME, data['app_name'])


class TitleDelimiterTests(AbstractContextProcessorTest):
    def test_title_delimiter_is_read_from_settings(self):
        request = self.factory.get('/')
        data = title_delimiter(request)
        self.assertEqual(settings.APP_TITLE_DELIMITER, data['title_delimiter'])
