from socket import *

#1、创建套接字
udpsocket = socket(AF_INET,SOCK_DGRAM)
#2、绑定端口
udpsocket.bind(('',7788))
#3、等待接收数据

while True:
    recvfData = udpsocket.recvfrom(1024)
    #4、显示接收
    content = []
    content0,destinfo = recvfData
    #5、获取消息中的数据和端口地址
        #将字符串转换为列表
    content = list(eval(content0.decode('utf-8')))
    print(content)
    #6、从列表中将数据、目标IP、目标端口获取到
    recv_message, recv_Addr, recv_Port = content
    #7、组合要发送的消息，包括消息来源
    recv_message = str(recv_Addr) + ":" + str(recv_Port) + "说:" + recv_message
    print(recv_message)
    #5、发送数据到目标
    udpsocket.sendto(recv_message.encode('utf-8'),(recv_Addr,recv_Port))
    print("----end---------")
