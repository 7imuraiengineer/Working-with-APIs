import requests
from datetime import datetime, timedelta
# Make the API request


def quyosh_vaqti(url, parametres):
    response = requests.get(url, params=parametres)
    data = response.json()
    kunchb = ["sunrise", "sunset"]
    times = {i: data['sys'][i] for i in kunchb}
    for i, time in times.items():
        global_time = datetime.fromtimestamp(time)
        local_time = global_time + timedelta(hours=-5)
        time = local_time.strftime('%H:%M')
        times[i] = time
    return f"Quyosh chiqishi vaqti: {times['sunrise']}, Quyosh botishi vaqti: {times['sunset']}"