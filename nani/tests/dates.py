from nani.test_utils.data import DATES_REVERSED, D3
from nani.test_utils.testcase import NaniTestCase
from testproject.app.models import Date

class LatestTests(NaniTestCase):
    fixtures = ['dates.json']
    
    def test_shared_latest(self):
        latest = Date.objects.language('en').latest('shared_date')
        self.assertEqual(latest.pk, DATES_REVERSED[D3]['shared_date'])
        
    def test_translated_latest(self):
        latest = Date.objects.language('en').latest('translated_date')
        self.assertEqual(latest.pk, DATES_REVERSED[D3]['translated_date_en'])
        latest = Date.objects.language('ja').latest('translated_date')
        self.assertEqual(latest.pk, DATES_REVERSED[D3]['translated_date_ja'])

class DatesTests(NaniTestCase):
    fixtures = ['dates.json']
    def test_objects_dates(self):
        self.assertEqual(len(Date.objects.language('en').dates("shared_date", "year")), 2)
        self.assertEqual(len(Date.objects.language('en').dates("shared_date", "month")), 3)
        self.assertEqual(len(Date.objects.language('en').dates("shared_date", "day")), 3)