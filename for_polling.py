from requests import get
import configparser


def polling(polling_token, polling_update_id):
    while True:
        data = \
            get(f'https://api.telegram.org/bot{polling_token}/getUpdates?timeout=4&offset={polling_update_id}').json()[
                'result']
        if data:
            polling_update_id = data[0]['update_id'] + 1
            return data[0], polling_update_id


def start_data():
    config = configparser.ConfigParser()  # создаём объект парсера
    config.read("settings.ini")  # читаем конфиг
    token = config["bot"]["token"]
    update_id = 0
    return token, update_id
