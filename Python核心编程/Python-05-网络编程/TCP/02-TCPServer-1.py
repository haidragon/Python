from socket import *
from threading import Thread

#创建套接字
TCPServer = socket(AF_INET, SOCK_STREAM)
#绑定IP
TCPServer.bind(("",7788))
#重复使用绑定的服务器，若服务器先结束2MSL时间之内，使用如下代码可直接使用上次绑定的端口
TCPServer.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#侦听端口
#使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，listen(5)表示最大可以连接5个client
#linux中listen(5)写几没啥用
TCPServer.listen(5)
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# newSocket⽤来为这个客户端服务
# tcpSerSocket就可以省下来专⻔等待其他新客户端的链接

def recvMessage(newClient):
        print("--------开始监听-------------")
        while True:
            recvData = newClient.recv(1024)
            if len(recvData) > 0:
                print(recvData)
                content = list(eval(recvData.decode('utf-8')))
                ip, port, message = content
                print("收到数据，IP=%s,Port=%s,message=%s" % (ip, port, message))
                TCPClient = connectSend(ip, int(port))
                sendMessge(TCPClient, message)
            else:
                print("recv Data is empty")
                break
        newClient.close()

def connectSend(ip,port):
    print("--------开始连接客户端服务器-------------")
    # 创建套接字-发布
    TCPClient = socket(AF_INET, SOCK_STREAM)
    # 连接到服务器
    sendAddr = (ip,port)
    TCPClient.connect(sendAddr)
    return TCPClient

def sendMessge(TCPClient,sendData):
    #while True:
    #sendData = input("shuruyidianshaba")
    print("--------开始发布送数据至目标服务器-------------")
    TCPClient.send(sendData.encode('utf-8'))
    print("--------发布送数据至目标服务器成功-------------")

def main():
    while True:
        #可以保证在创建线程前必然有连接过来，如果把accept放在线程中，会导致线程爆掉
        newClient, clientAddr = TCPServer.accept()
        recv = Thread(target=recvMessage,args=(newClient, ))
        recv.start()
        #recv.join()


if __name__ == '__main__':
    main()
