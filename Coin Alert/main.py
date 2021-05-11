import requests
import pandas as pd
import json
from playsound import playsound

key_val = '30ff33f6-a3a5-424f-80fc-ed567f661057'
api_endpoint = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
api_endpoint += key_val


def getData()
    json_data = requests.get(api_endpoint).json()
    crypto_data = json_data['data']

    for c in crypto_data:
        if c['name'] == "Bitcoin":
            price = c['quote']['USD']['price']
            return price


while True:
    if getData() >= 50000.0:
        print("yes")
        playsound('sound.WAV')
