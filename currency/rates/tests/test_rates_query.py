import graphene
import mock

from currency.schema import Query
from currency.tests.base import BaseTestCase
from currency.utils.commons import read_json
from currency.rates.tests.test_rates_api import FIXTURES_PATH
from currency.utils.patch.fixer_api_patch import FixerApiPatch


class TestRatesQuery(BaseTestCase):

    def setUp(self):
        super(TestRatesQuery, self).setUp()

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
