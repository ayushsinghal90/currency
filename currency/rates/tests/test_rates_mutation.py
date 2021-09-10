import graphene
import mock

from currency.schema import Mutation
from currency.tests.base import BaseTestCase
from currency.utils.commons import read_json
from currency.rates.tests.test_rates_api import FIXTURES_PATH
from currency.utils.patch.fixer_api_patch import FixerApiPatch


class TestGetRatesQuery(BaseTestCase):

    def setUp(self):
        super(TestGetRatesQuery, self).setUp()

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
