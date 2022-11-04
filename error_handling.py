from traceback import format_exc
import datetime


def error_massage():
    file = open('logs.txt', "a")
    file.write(f'----------------------------------------\n{datetime.datetime.now()}\n {format_exc()}\n')
    file.close()