import logging

from django.test import SimpleTestCase
from django.test.client import Client

LOG = logging.getLogger(__name__)


class BaseTestCase(SimpleTestCase):

    def _get(self, url, data=None, data_format='application/json'):
        """
        Makes get request to the specified url
        """
        client = Client()
        data = client._encode_json({} if data is None else data, data_format)
        post_data = client._encode_data(data, data_format)

        return client.generic('GET', url, post_data, data_format)

    def _post(self, url,  data=None, data_format='application/json'):
        """
        Makes post request with data to the specific urls
        """
        return Client().post(url, data=data, content_type=data_format)
