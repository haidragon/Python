from socket import *
from threading import Thread

#1、创建套接字
udpsocket = socket(AF_INET,SOCK_DGRAM)
#2、绑定端口
udpsocket.bind(('',7790))
#3、接收数据
def recv():
    while True:
        print("recv")
        recvfData = udpsocket.recvfrom(1024)
        print(recvfData)
        # 4、显示接收
        content0, destinfo = recvfData
        print(content0.decode('utf-8'))

def send():
    while True:
        # 2、准备接收方地址
        sendAddress = ('192.168.0.20', 7788)
        # 3、从键盘获取数据
        message = input("请输入")
        sendData = []
        sendData.append(message)
        sendData.append('192.168.0.20')
        sendData.append(7789)
        # 4、发送数据到指定电脑
        udpsocket.sendto(str(sendData).encode('utf-8'), sendAddress)
        #udpsocket.sendto(sendData, sendAddress)
if __name__ == '__main__':
    thread1 = Thread(target=send)
    thread2 = Thread(target=recv)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()