import mock

from currency.rates.constants import RATES_KEY
from currency.scheduled_task.tasks import currency_sync_engine
from currency.tests.base import BaseTestCase
from currency.utils.patch.fixer_api_patch import FixerApiPatch
from django.test import override_settings

from currency.utils.redis_helper import RedisUtilities


class TestTasks(BaseTestCase):
    def setUp(self):
        super(TestTasks, self).setUp()

    @mock.patch('currency.utils.fixer_api.FixerApi.get_latest_rates', FixerApiPatch.get_latest_rates_patch)
    @override_settings(CURRENCY_PAIRS_TO_SYNC=["EUR-USD", "EUR-INR", "EUR-JPY"])
    def test_task_currency_sync_engine(self):
        currency_sync_engine()
        eur_usd = RedisUtilities.get(RATES_KEY.format(base="EUR", symbol="USD"))
        self.assertIsNotNone(eur_usd)

        eur_inr = RedisUtilities.get(RATES_KEY.format(base="EUR", symbol="INR"))
        self.assertIsNotNone(eur_inr)

        eur_jpy = RedisUtilities.get(RATES_KEY.format(base="EUR", symbol="JPY"))
        self.assertIsNotNone(eur_jpy)

    @mock.patch('currency.utils.fixer_api.FixerApi.get_latest_rates', FixerApiPatch.get_latest_rates_failed_patch)
    @override_settings(CURRENCY_PAIRS_TO_SYNC=["IND-USD", "IND-INR", "IND-JPY"])
    def test_task_currency_sync_engine_failure(self):
        currency_sync_engine()
        ind_usd = RedisUtilities.get(RATES_KEY.format(base="IND", symbol="USD"))
        self.assertIsNone(ind_usd)

        ind_inr = RedisUtilities.get(RATES_KEY.format(base="IND", symbol="INR"))
        self.assertIsNone(ind_inr)

        ind_jpy = RedisUtilities.get(RATES_KEY.format(base="IND", symbol="JPY"))
        self.assertIsNone(ind_jpy)
