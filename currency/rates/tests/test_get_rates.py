import mock

from currency.tests.base import BaseTestCase
from currency.utils.commons import read_json
from currency.utils.patch.fixer_api_patch import FixerApiPatch

FIXTURES_PATH = 'currency/rates/tests/fixtures/{file_path}'


class TestGetRates(BaseTestCase):

    def setUp(self):
        super(TestGetRates, self).setUp()

    @mock.patch('currency.utils.fixer_api.FixerApi.get_latest_rates', FixerApiPatch.get_latest_rates_patch)
    def test_get_rates(self):
        data = read_json(FIXTURES_PATH.format(file_path='get_rates_body.json'))
        response = self._get('/rate/', data)
        self.assertEqual(201, response.status_code)

    @mock.patch('currency.utils.fixer_api.FixerApi.get_latest_rates', FixerApiPatch.get_latest_rates_patch)
    def test_get_rates_2(self):
        data = read_json(FIXTURES_PATH.format(file_path='get_rates_body.json'))
        response = self._post('/rates/', data)