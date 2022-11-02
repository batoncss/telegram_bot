from requests import get


def text_for_joke():
    page = get("https://www.anekdot.ru/random/anekdot/")
    data = page.text
    find_start = data.find('<div class="text">')
    find_finish = data.find('</div>', find_start)
    text = ""
    for i in range(find_start + 18, find_finish):
        if data[i] == "<":
            text += "\n"
        elif data[i] == "b" or data[i] == "r" or data[i] == ">":
            text += ""
        else:
            text += data[i]
    return text
