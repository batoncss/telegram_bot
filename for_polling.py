from requests import get
import configparser
from pathlib import Path


def polling(polling_token, polling_update_id):
    while True:
        data = get(f'https://api.telegram.org/bot{polling_token}/getUpdates?timeout=4&offset={polling_update_id}').json()['result']
        if data:
            polling_update_id = data[0]['update_id'] + 1
            return data[0], polling_update_id


def start_data():
    config = configparser.ConfigParser()  # создаём объект парсера
    config.read(Path(Path.cwd(), 'settings.ini'))  # указываем полный адрес конфига в зависимости от системы и читаем его
    token = config["bot"]["token"]
    update_id = 0
    return token, update_id
