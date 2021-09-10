import mock

from currency.tests.base import BaseTestCase
from currency.utils.commons import read_json
from currency.utils.patch.fixer_api_patch import FixerApiPatch
from currency.utils.api_response_messages import INPUT_INVALID_MSG

FIXTURES_PATH = 'currency/rates/tests/fixtures/{file_path}'


class TestRatesApi(BaseTestCase):

    def setUp(self):
        super(TestRatesApi, self).setUp()

    @mock.patch('currency.utils.fixer_api.FixerApi.get_latest_rates', FixerApiPatch.get_latest_rates_patch)
    def test_get_rates(self):
        data = read_json(FIXTURES_PATH.format(file_path='get_rates_body.json'))
        response = self._get('/rate/', data)
        self.assertEqual(201, response.status_code)

    def test_get_rates_without_body(self):
        response = self._get('/rate/')
        self.assertEqual(401, response.status_code)
        self.assertEqual(INPUT_INVALID_MSG, response.data['message'])

    @mock.patch('currency.utils.fixer_api.FixerApi.get_latest_rates', FixerApiPatch.get_latest_rates_failed_patch)
    def test_get_rates_fixer_api_failure(self):
        data = read_json(FIXTURES_PATH.format(file_path='error_get_rates_body.json'))
        response = self._get('/rate/', data)
        self.assertEqual(500, response.status_code)
