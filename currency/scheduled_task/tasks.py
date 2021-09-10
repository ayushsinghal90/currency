from celery import shared_task
from django.conf import settings

from currency.rates.utils import fetch_and_save_rate
from currency.utils.redis_helper import RedisUtilities


@shared_task
def currency_sync_engine():
    """
    Task to fetch latest pair rates that are mandatory to be in the cache
    :return:
    """
    pairs = settings.CURRENCY_PAIRS_TO_SYNC
    pair_to_sync = {}

    for pair in pairs:
        pair_rate = RedisUtilities.get(pair)
        if pair_rate is None:
            pair_split = pair.split('-')

            base = pair_split[0]
            if base not in pair_to_sync:
                pair_to_sync[base] = []

            pair_to_sync[base].append(pair_split[1])

    for base in pair_to_sync:
        fetch_and_save_rate(base, pair_to_sync[base])
