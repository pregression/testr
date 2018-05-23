from django.test import TestCase
from re import search

from core.models import CspReport

class CspReportTests(TestCase):
    def test_will_convert_report_string_into_dict(self):
        s = '{"foo":"bar"}'
        r = CspReport.objects.create(report=s)
        self.assertIsInstance(r.report, dict)

    def test_str_representation_will_have_the_id_and_created_time(self):
        d = {"foo": "bar"}
        r = CspReport.objects.create(report=d)
        re = r"CSP Report:\s*\d*\s*at\s*\d{4}\-\d{2}\-\d{2}\s*\d{2}\:\d{2}\:\d{2}\.\d*\+\d{2}\:\d{2}"
        self.assertTrue(search(re, str(r)))
