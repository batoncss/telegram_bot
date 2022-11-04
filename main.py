from requests import get
from for_polling import polling, start_data
from for_message import processing, for_bot_text
from error_handling import error_massage


token, update_id = start_data()
while True:
    try:
        data_for_processing, update_id = polling(token, update_id)
        user, chat, user_text = processing(data_for_processing)
        bot_text = for_bot_text(user_text)
        data = get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat}&text={bot_text}')
    except:
        error_massage()
