from socket import *

#创建套接字
tcpCLient = socket(AF_INET,SOCK_STREAM)
#连接服务器
tcpCLient.connect(("192.168.230.241",7788))
sendData = input("请输入")
#发送数据
tcpCLient.send(sendData)
#接收返回
recvData = tcpCLient.recv(1024)
print(recvData)

tcpCLient.close()



