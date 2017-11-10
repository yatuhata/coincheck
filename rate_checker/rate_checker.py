from __future__ import absolute_import
import time
import requests


class CoincheckClient:
    '''
        Coincheck API Client
    '''
    URL = 'https://coincheck.com/api'

    def get_rate(self):
        rate = requests.get(self.URL + '/rate/btc_jpy').json()
        print('%s' % rate)


# Check rate with Coincheck API per 1 seconds
client = CoincheckClient()
while True:
    client.get_rate()
    time.sleep(1)
