from currency.utils.commons import read_json

PATH_RESPONSE_PATH = 'currency/utils/patch/response/{file_name}.json'


class FixerApiPatch:

    @staticmethod
    def get_latest_rates_patch(base, symbols):
        return read_json(PATH_RESPONSE_PATH.format(file_name='get_latest_api'))

    @staticmethod
    def get_latest_rates_failed_patch(base, symbols):
        response = read_json(PATH_RESPONSE_PATH.format(file_name='get_latest_api_failed'))
        raise Exception(response['error']['type'])
