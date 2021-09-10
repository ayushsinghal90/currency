from currency.utils.commons import read_json


class FixerApiPatch:
    @staticmethod
    def get_latest_rates_patch(base, symbols):
        return read_json('currency/utils/patch/get_latest_api_response.json')
