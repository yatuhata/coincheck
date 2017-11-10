from __future__ import absolute_import
import time


# Coincheck API Client
class CoincheckClient:
    def get_rate(self):
        print("hogehoge")


# Check rate with Coincheck API per 10 seconds
client = CoincheckClient()
while True:
    client.get_rate()
    time.sleep(10)
    