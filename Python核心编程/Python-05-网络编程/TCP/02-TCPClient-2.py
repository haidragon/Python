from socket import *
from threading import Thread

def recvMessage(newClient):
    while True:
        recvData = newClient.recv(1024)
        if len(recvData) > 0:
            print(recvData)
        else:
            print("recv Data is empty")
            break
    newClient.close()


def sendMessge(TCPClient):
    while True:
        sendData = []
        ip = input("IP>>")
        port = input("端口>>")
        s = input("内容>>")
        sendData.append(ip)
        sendData.append(port)
        sendData.append(s)
        TCPClient.send(str(sendData).encode('utf-8'))

def connectSend():
    # 创建套接字-发布
    TCPClient = socket(AF_INET, SOCK_STREAM)
    # 连接到服务器
    #TCPClient.connect(("192.168.230.241", 7788))
    #TCPClient.connect(("192.168.109.130", 7788))
    TCPClient.connect(("127.0.0.1", 7788))

    return TCPClient

def connectRecv():
    # 创建套接字-接收数据
    TCPServer = socket(AF_INET, SOCK_STREAM)
    # 绑定IP
    TCPServer.bind(("", 7789))
    # 侦听端口
    # 使⽤socket创建的套接字默认的属性是主动的，使⽤listen将其变为被动的
    TCPServer.listen(5)
    return TCPServer

def main():
    TCPServer = connectRecv()
    TCPClient = connectSend()
    while True:
        send = Thread(target=sendMessge, args=(TCPClient, ))
        send.start()
        newClient, clientAddr = TCPServer.accept()
        recv = Thread(target=recvMessage, args=(newClient, ))

        recv.start()
        send.join()
        recv.join()
    TCPServer.close()
    TCPClient.close()

if __name__ == '__main__':
    main()
