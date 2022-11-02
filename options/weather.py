from requests import get


def text_for_weather():
    site = "https://world-weather.ru/pogoda/russia/saint_petersburg/"
    city_find = "|Санкт-Петербург|"
    page = get(site)
    data = page.text
    find_start_false = data.find(city_find)
    find_start = data.find("|", find_start_false + 1, )
    find_finish = data.find("|", find_start + 1, )
    number = ""
    for i in range(find_start + 1, find_finish):
        number += data[i]
    return f'Погода в Санкт-Петербурге: {number}°C'