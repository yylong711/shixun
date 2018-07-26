import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建tcp连接
sock.bind(('127.0.0.1', 9000))

sock.listen(5)
connection, address = sock.accept()

print(address)

while True:
    try:
        data = connection.recv(1024)
        if data:
            connection.send('hello ni hao'.encode('utf-8'))
        time.sleep(3)
    except socket.timeout:
        print ('socket connection timeout')