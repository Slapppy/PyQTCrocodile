import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.bind(('', 2668))  # связываем сокет с портом, где он будет ожидать сообщения
sock.listen(10)  # указываем сколько может сокет принимать соединений
print('Server is running, please, press ctrl+c to stop')

server_data = []

clientConnection, clientAddress = sock.accept()
words = ['car' , 'human']
random_num = random.choice(words)

word = clientConnection.send(random_num.encode())








while True:
    print('connected:', clientAddress)
    data = clientConnection.recv(2048).decode()
    server_data.append(data)
    print(server_data)
    print(str(data))
    if str(data) == random_num:
        clientConnection.close()
    print(server_data)
    print(str(data))
clientConnection.close()  # закрываем соединение


