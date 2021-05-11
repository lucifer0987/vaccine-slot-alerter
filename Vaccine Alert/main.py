import requests
import json
from playsound import playsound
import time

api_endpoint_1 = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=241&date=11-05-2021'
api_endpoint_2 = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=331&date=11-05-2021'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def getData(api_endpoint):
    print(requests.get(api_endpoint, headers=headers))
    json_Data = requests.get(api_endpoint, headers=headers).json()
    center_Data = json_Data['centers']

    res = 0
    for c in center_Data:
        session = c['sessions']
        for s in session:
            if s['min_age_limit'] == 18:
                if s['available_capacity'] > 0:
                    print(c['state_name'])
                    res += 1

    print(c['state_name'])
    if res > 0:
        return True


# Program Code Starts
while True:
    print("\n\n")
    try:
        if getData(api_endpoint_1):
            break
        if getData(api_endpoint_2):
            break
        print("NO Error")
        time.sleep(10)
    except Exception as e:
        print("Error", str(e))
        print(Exception)
        time.sleep(10)


# Slot Found
while True:
    playsound('sound.WAV')
