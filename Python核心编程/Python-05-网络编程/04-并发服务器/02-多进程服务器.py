from socket import *
from multiprocessing import Process
#from multiprocessing import Pool

'''
通过为每个客户端创建一个进程的方式，能够同时为多个客户端进行服务
当客户端不是特别多的时候，这种方式还行，如果有几百上千个，就不可取了，因为每次创建进程等过程需要好较大的资源
'''

def dealWithClient(newsocket, destAddr):
    while True:
        try:
            recvData = newsocket.recv(1024)
        except Exception as s:
            print(s)
            break

        if len(recvData) > 0:
            print('recv[%s]:%s' % (str(destAddr), recvData))
        else:
            print('[%s]客户端已经关闭' % str(destAddr))
            break
    #数据接收完成后关闭socket连接
    newsocket.close()
        #p.close()

def main():
    # 创建TCP的socket连接
    serSocket = socket(AF_INET, SOCK_STREAM)

    # 重复使用绑定信息
    # setsockopt() 设置选项，与之对应的还有getsockopt()：得到设置
    # setsockopt(level,optname,value)
    # 重复使用绑定的服务器，若服务器先结束2MSL时间之内，使用如下代码可直接使用上次绑定的端口
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serSocket.bind(("", 7788))
    serSocket.listen(5)
    #p = Pool(5)
    try:
        while True:
            print('-----主进程，，等待新客户端的到来------')
            newsocket, destAddr = serSocket.accept()
            print('-----主进程，，接下来创建一个新的进程负责数据处理[%s]-----' % str(destAddr))
            #p.apply_async(dealWithClient, (newsocket, destAddr, p))
            client = (target=dealWithClient, args=(newsocket, destAddr, ))
            client.start()
            #因为已经向子进程中copy了一份（引用），并且父进程中这个套接字也没有用处了，所以关闭掉
            newsocket.close()
    finally:
        # 当为所有的客户端服务完之后再进行关闭，表示不再接收新的客户端的链接
        serSocket.close()

if __name__ == '__main__':
    main()
