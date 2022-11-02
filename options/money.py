from requests import get


def exchange_rate(currency):
    data = get('https://cbr.ru/currency_base/daily/').text
    word_for_find = currency + '</td>'
    false_start = data.find(word_for_find)
    start = data.find('<td>', false_start + len(word_for_find))
    finish = data.find('</td>', start + 5)
    answer = ""
    for i in range(start + 4, finish):
        answer += data[i]
    return answer


def text_for_money():
    return f"Курсы иностранных валют к рублю\nДоллар США: {exchange_rate('Доллар США')}\nЕвро: {exchange_rate('Евро')}"