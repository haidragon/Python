from socket import *
import time

g_socketList = []

def main():
    #创建套接字
    serSocket = socket(AF_INET, SOCK_STREAM)
    #设置socket
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #绑定端口
    bindAddr = ("", 7788)
    serSocket.bind(bindAddr)
    #监听
    serSocket.listen(5)
    #设置为非阻塞
    serSocket.setblocking(False)
    

    while True:
        try:
            newClientInfo = serSocket.accept()
        except Exception as s:
            #print("==========1===>%s"%str(s))
            pass
        else:
            print("一个新的客户端到来:%s" % str(newClientInfo))
            newClientInfo[0].setblocking(False)
            g_socketList.append(newClientInfo)

        #存放需要删除的socket
        needDelClientInfoList = []

        for clientSocket,clientAddr in g_socketList:
            try:
                recvData = clientSocket.recv(1024)
                if len(recvData) > 0:
                    print('recv[%s]:%s' % (str(clientAddr), recvData))
                else:
                    clientSocket.close()
                    #needDelClientInfoList.append((clientSocket, clientAddr))
                    g_socketList.remove((clientSocket, clientAddr))
                    print('[%s]客户端已经关闭' % str(clientAddr))
            except Exception as s:
                #print("==========2===>%s" % str(s))
                pass


        for needDelClientInfo in needDelClientInfoList:
            g_socketList.remove(needDelClientInfo)


if __name__ == '__main__':
    main()