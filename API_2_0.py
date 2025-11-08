import requests
from datetime import datetime, UTC, timedelta
# Make the API request

url = "https://api.openweathermap.org/data/2.5/weather"

parametres = {
    'q': 'Tashkent',
    'appid': '7c43be754b25a6c3c095335ccb16b232',
    'units': 'metric'
    }

response = requests.get(url, params=parametres)
data = response.json()

time = data['sys']['sunrise']

global_time = datetime.fromtimestamp(time)
local_time = global_time + timedelta(hours=-5)
time = local_time.strftime('%H:%M')

print(time)



