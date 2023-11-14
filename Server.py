import socket
import json

# Серверные настройки
#Локальный хост, чтобы запустить всё на одном пк, можно поставить виртуальную машину, чтобы приблизиться к реальным условиям
HOST = '127.0.0.1'
#Порт случайный из свободных
PORT = 65432
#cоздаем сервер, который будет ожидать запрос от клиента ,далее будем проверять строку
# Создаем сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#Тут мы с вами сервер привязываем с хостом и портом и начинаем "слушать"
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Получено соединение с', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break

            # Проверяем, является ли полученная строка  JSON в зависемости от результата присваем TRUE /FALSE
            try:
                json_object = json.loads(data)
                response = True
            except ValueError as e:
                response = False

            # Отправляем результат клиенту
            conn.sendall(str(response).encode())

