from __future__ import absolute_import
import time
import datetime
import requests
from influxdb import InfluxDBClient


class CoincheckClient:
    '''
        Coincheck API Client
    '''
    URL = 'https://coincheck.com/api'

    def get_rate(self):
        return requests.get(self.URL + '/rate/btc_jpy').json()


if __name__ == '__main__':
    # Setting
    coincheck_client = CoincheckClient()
    influxdb_client = InfluxDBClient(
        host='localhost',
        port=8086,
        username='root',
        password='root',
        database='coincheck'
    )
    influxdb_client.create_database('coincheck')

    # Check rate with Coincheck API
    data = coincheck_client.get_rate()
    json_body = [
        {
            "measurement": "rate",
            "time": datetime.datetime.now().isoformat('T'),
            "fields": {
                "btc_jpy": float(data['rate'])
            }
        }
    ]
    influxdb_client.write_points(json_body)
