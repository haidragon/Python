from socket import *
from threading import Thread


#创建套接字
TCPServer = socket(AF_INET, SOCK_STREAM)
#绑定IP
TCPServer.bind(("",7788))
#侦听端口
#使⽤socket创建的套接字默认的属性是主动的，使⽤listen将其变为被动的
TCPServer.listen(5)
# 如果有新的客户端来链接服务器，那么就产⽣⼀个信⼼的套接字专⻔为这个客户端服务器
# newSocket⽤来为这个客户端服务
# tcpSerSocket就可以省下来专⻔等待其他新客户端的链接

def recvMessage(newClient):
    while True:
        recvData = newClient.recv(1024)
        if len(recvData) > 0:
            print(recvData)
        else:
            print("recv Data is empty")
            break

def sendMessge(newClient):
    while True:
        sendData = input("shuruyidianshaba")
        newClient.send(sendData.encode('utf-8'))

def main():
    while True:
        newClient, clientAddr = TCPServer.accept()
        send = Thread(target=sendMessge, args=(newClient, ))
        recv = Thread(target=recvMessage, args=(newClient, ))
        send.start()
        recv.start()
        send.join()
        recv.join()
        newClient.close()


if __name__ == '__main__':
    main()
