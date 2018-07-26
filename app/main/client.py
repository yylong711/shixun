import socket
import time


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        print('客户端被分配了socket名称', self.sock.getsockname())
        # 创建tcp连接

    def send_message(self, message):
        print('客户端开始发送')
        self.sock.sendall(message.encode('utf-8'))

    # 接受数据的长度 和sock类对象
    def recvall(self, sock, length):
        mesg = sock.recv(length)
        print(mesg)
        print(type(mesg))
        print(mesg.decode('utf-8'))
        return mesg


    def receive(self):
        i=1
        while True:
            reply = self.recvall(self.sock, 1024)
            if reply:
                self.sock.close()
                return reply
            i+=1
            if i>1000:
                break

if __name__ == '__main__':



    client = Client('localhost',1234)
    client.send_message('1我今天很开心')
    client.receive()
