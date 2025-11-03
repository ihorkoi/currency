import requests
from requests.exceptions import HTTPError


class Currency():
    def __init__(self, headers=None, base_currency='USD'):
        self.url = 'https://api.currencyapi.com/v3/latest'
        self.base_currency = base_currency
        if headers is None:
            headers = {
                'apikey': 'cur_live_JZgFOek59tXv7CXYlWUrKn7Z62U18OAp33qxJ4js'}
        self.headers = headers

    def fetch_data(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            self.response_json_ = response.json()
            return self.response_json_
        except HTTPError as err:
            print(f"HTTP error occured: {err}")

    def get_rate(self, currency_from, currency_to):
        data = self.fetch_data()['data']
        try:
            currency_to_value = data[currency_to]['value']
            currency_from_value = data[currency_from]['value']

            return currency_to_value / currency_from_value
        except KeyError:
            print('No such currency')

    def convert(self, amount, currency_from, currency_to):
        return amount * self.get_rate(currency_from, currency_to)
