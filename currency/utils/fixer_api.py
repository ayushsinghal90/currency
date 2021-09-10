import logging
import requests

from django.conf import settings

LOG = logging.getLogger(__name__)


class FixerApi:

    @staticmethod
    def get_latest_rate_url():
        return "{fixer_url}latest".format(fixer_url=settings.FIXER_URL)

    @staticmethod
    def get_latest_rates(base, symbols):
        params = {
            'access_key': settings.FIXER_API_KEY,
            'base': base,
            'symbols': ",".join(symbols),
        }

        response = requests.get(FixerApi.get_latest_rate_url(), params)
        response = response.json()
        LOG.info(response)

        if not bool(response['success']):
            raise Exception(response['error']['type'])

        return response
