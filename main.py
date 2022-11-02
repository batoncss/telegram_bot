from requests import get
from for_polling import polling, start_data
from for_message import processing, for_bot_text


token, update_id = start_data()
while True:
    data_for_processing, update_id = polling(token, update_id)
    user, chat, user_text = processing(data_for_processing)
    bot_text = for_bot_text(user_text)
    data = get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat}&text={bot_text}')
