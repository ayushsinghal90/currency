import graphene
import mock

from currency.schema import Query, Mutation
from currency.tests.base import BaseTestCase
from currency.utils.api_response_messages import INPUT_INVALID_MSG
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

    def test_get_rates_without_body(self):
        response = self._get('/rate/')
        self.assertEqual(401, response.status_code)
        self.assertEqual(INPUT_INVALID_MSG, response.data['message'])

    @mock.patch('currency.utils.fixer_api.FixerApi.get_latest_rates', FixerApiPatch.get_latest_rates_failed_patch)
    def test_get_rates_fixer_api_failure(self):
        data = read_json(FIXTURES_PATH.format(file_path='error_get_rates_body.json'))
        response = self._get('/rate/', data)
        self.assertEqual(500, response.status_code)

    @mock.patch('currency.utils.fixer_api.FixerApi.get_latest_rates', FixerApiPatch.get_latest_rates_patch)
    def test_get_rates_query(self):
        schema = graphene.Schema(query=Query)
        result = schema.execute(
            """{rates(base: "EUR", symbols: ["JPY","USD","INR"]){base,rates {symbol,rate,base}}}""")
        self.assertIsNone(result.errors)

        response = read_json(FIXTURES_PATH.format(file_path='get_rates_query_response.json'))

        self.assertDictEqual(response, result.data)

    @mock.patch('currency.utils.fixer_api.FixerApi.get_latest_rates', FixerApiPatch.get_latest_rates_failed_patch)
    def test_get_rates_query_failure(self):
        schema = graphene.Schema(query=Query)
        result = schema.execute(
            """{rates(base: "IND", symbols: ["JPY","USD","INR"]){base,rates {symbol,rate,base}}}""")
        self.assertIsNotNone(result.errors)

        self.assertDictEqual({'rates': None}, result.data)

    @mock.patch('currency.utils.fixer_api.FixerApi.get_latest_rates', FixerApiPatch.get_latest_rates_patch)
    def test_update_rates_mutation(self):
        schema = graphene.Schema(mutation=Mutation)
        result = schema.execute(
            """mutation updateRates{updateRates(base: "EUR", symbols: ["JPY","USD","INR"])
            {ok,currencyRates{base,rates {symbol,rate,base}}}}""")
        self.assertIsNone(result.errors)

        response = read_json(FIXTURES_PATH.format(file_path='update_rates_mutation_response.json'))

        self.assertDictEqual(response, result.data.get('updateRates'))

    @mock.patch('currency.utils.fixer_api.FixerApi.get_latest_rates', FixerApiPatch.get_latest_rates_failed_patch)
    def test_update_rates_mutation_failure(self):
        schema = graphene.Schema(mutation=Mutation)
        result = schema.execute(
            """mutation updateRates{updateRates(base: "IND", symbols: ["JPY","USD","INR"])
            {ok,currencyRates{base,rates {symbol,rate,base}}}}""")

        self.assertDictEqual({'currencyRates': None, 'ok': False}, result.data.get('updateRates'))
