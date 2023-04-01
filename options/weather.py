from requests import get


def text_for_weather():
    site = "https://world-weather.ru/pogoda/russia/saint_petersburg/"
    headers = {'user-agent': 'my-app/0.0.1'}
    page = get(site, headers=headers)
    data = page.text
    find_start = data.find('weather-now-number">') + 20
    find_finish = data.find('<', find_start + 1, )
    number = ""
    for i in range(find_start, find_finish):
        number += data[i]
    return f'Погода в Санкт-Петербурге: {number}°C'
