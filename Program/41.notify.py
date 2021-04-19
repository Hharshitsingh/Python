import requests
from win10toast import ToastNotifier
import time
url = "https://api.covid19india.org/state_district_wise.json"

def update():
    response = requests.get(url)
    data = response.json()['Punjab']['districtData']['Ludhiana']
    # print(data)
    text = f'''Confirmed Cases: {data['confirmed']}\nRecovered: {data['recovered']}\nDeath: {data['deceased']}'''
    # print(text)
    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid Ludhiana Update", text, duration=10)
        time.sleep(60)

update()