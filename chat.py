import requests, threading

server = input('Введите сервер:\n>> ')
name = input('Ваше имя:\n>> ')

def get_new_mes():
    old = requests.get(f'{server}/check').text
    while True:
        get = requests.get(f'{server}/check').text
        if old != get:
            old = get
            print(get)

rT = threading.Thread(target = get_new_mes)
rT.start()

while True:
    mes = input('')
    requests.get(f'{server}/chat/{name}/{mes}')
    
