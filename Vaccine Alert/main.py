import requests
import json
from playsound import playsound
import time

pincode = ['825409', '825109']
api_endpoint_1 = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='
api_endpoint_2 = '&date=14-05-2021'
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
                if s['available_capacity'] > 5:
                    print(c)
                    print(c['state_name'])
                    print(c['district_name'])
                    print(c['pincode'])
                    res += 1

    print(c['pincode'])
    if res > 0:
        return True


# Program Code Starts
while True:
    print("\n\n")
    try:
        gotit = False
        for i in pincode:
            if getData(api_endpoint_1+i+api_endpoint_2):
                gotit = True
        if gotit:
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
