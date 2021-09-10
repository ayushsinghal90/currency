import logging

from currency.rates.constants import RATES_KEY, RATE_EXPIRE_TIME_IN_SECONDS
from currency.utils.fixer_api import FixerApi
from currency.utils.redis_helper import RedisUtilities

LOG = logging.getLogger(__name__)


def get_rates(base, symbols):
    fixer_rates = {}

    rates, symbols_to_cache = fetch_rate_from_cache(base, symbols)
    if len(symbols_to_cache) > 0:
        fixer_rates, is_success = fetch_and_save_rate(base, symbols)
        if not is_success:
            raise Exception("Can not find rate")

    return rates | fixer_rates


def fetch_rate_from_cache(base, symbols):
    rates = {}
    symbols_to_cache = []

    for symbol in symbols:
        pair_rate = RedisUtilities.get(RATES_KEY.format(base=base, symbol=symbol))
        if pair_rate:
            rates[symbol] = pair_rate
        else:
            symbols_to_cache.append(symbol)

    return rates, symbols_to_cache


def fetch_and_save_rate(base, symbols):
    try:
        latest_rates = FixerApi.get_latest_rates(base, symbols)
        rates = latest_rates['rates']

        for symbol in rates:
            value = rates[symbol]
            RedisUtilities.set(RATES_KEY.format(base=base, symbol=symbol),
                               value,
                               RATE_EXPIRE_TIME_IN_SECONDS)

        return rates, True
    except Exception as ex:
        LOG.error("Fetch and save Rates failed msg {}".format(ex), exc_info=True)
        return None, False
