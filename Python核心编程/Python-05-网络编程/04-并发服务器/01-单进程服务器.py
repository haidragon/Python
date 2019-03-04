from socket import *

#创建TCP的socket连接
serSocket = socket(AF_INET,SOCK_STREAM)

#重复使用绑定信息
#setsockopt() 设置选项，与之对应的还有getsockopt()：得到设置
#setsockopt(level,optname,value)
#重复使用绑定的服务器，若服务器先结束2MSL时间之内，使用如下代码可直接使用上次绑定的端口
serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
serSocket.bind(("",7788))
serSocket.listen(5)

while True:
    newsocket,destAddr = serSocket.accept()
    print("开始处理数据%s"%str(destAddr))
    try:
        recvData = newsocket.recv(1024)
        if len(recvData) > 0:
            print('recv[%s]:%s' % (str(destAddr), recvData))
        else:
            print('[%s]客户端已经关闭' % str(destAddr))
            break
    finally:
        newsocket.close()

serSocket.close()

