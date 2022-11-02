from options import joke, money, weather

def processing(data):
    user = data['message']['from']['id']
    chat = data['message']['chat']['id']
    text = data['message']['text']
    return user, chat, text


def for_bot_text(text):
    text = text.lower()
    text = text.replace('/','')
    if text == 'кек':
        text_for_return = 'Чебурек'
    elif text == 'start' or text == 'старт':
        text_for_return = 'Привет, меня зовут Дима\nЯ люблю готовить и путешествовать по стране\nИщу работу программистом на Python'
    elif text == 'информация' or text == 'info':
        text_for_return = 'Мои поделки: github.com/batoncss\nМой VK:vk.com/batoncss'
    elif text == 'анекдот' or text == 'joke':
        text_for_return = joke.text_for_joke()
    elif text == 'погода' or text == 'weather':
        text_for_return = weather.text_for_weather()
    elif text == 'деньги' or text == 'money':
        text_for_return = money.text_for_money()
    else:
        text_for_return = "Ну и что мне тебе на это ответить?"
    return text_for_return
