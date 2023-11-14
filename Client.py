import socket

# Клиентские настройки
# хост и порт тот же самый , чтобы смогли подключиться
HOST = '127.0.0.1'
PORT = 65432

# Отправляемая строка. Пока ещё не знаем JSON на или нет
data = '{"Test": "True", "Server": ,127.0.0.1 "city": "NN"}'

# Подключаемся к серверу
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
#Отправляем строчку
    s.sendall(data.encode())
    response = s.recv(1024)

print('Получен ответ:', response.decode())
