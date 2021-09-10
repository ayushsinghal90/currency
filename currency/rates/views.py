import logging

from rest_framework.views import APIView

from currency.rates.utils import get_rates
from currency.utils.commons import get_api_error_response, get_api_success_response
from currency.utils.api_response_messages import SUCCESS_MESSAGE, ERROR_MESSAGE, SUCCESS_CODE, INPUT_INVALID, SERVER_ERROR

LOG = logging.getLogger(__name__)


class RatesView(APIView):

    def get(self, request):
        try:
            base = request.data.get('base', None)
            symbols = request.data.get('symbols', None)
            if base is None or symbols is None:
                return get_api_error_response(status=401, message=ERROR_MESSAGE[INPUT_INVALID])

            rates = get_rates(base, symbols)
            return get_api_success_response(data={"base": base, "rates": rates},
                                            message=SUCCESS_MESSAGE[SUCCESS_CODE],
                                            status=201)

        except Exception as e:
            LOG.error("Key addition failed {}".format(e), exc_info=True)
            return get_api_error_response(status=500,
                                          message=ERROR_MESSAGE[SERVER_ERROR])
