import struct
import os
from socket import *

def main():
    # 不管电脑是大端还是小端，统一按照大端组织字节序
    # !表示这是一个网络字节序，需要传输到网络
    # H表示占两个字节，两个H则表示占4个字节
    # s表示占一个字节，ns表示占n个字节
    # b表示占一个字节
    # Python3中，pack中的字符串需要用utf-8编码，不然会报错
    sendData = struct.pack("!H8sb5sb",1,"test.jpg".encode('utf-8'),0,"octet".encode('utf-8'),0)
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    #发送下载文件的请求
    udpSocket.sendto(sendData,("192.168.0.20",69))
    flag = True #表示能够下载数据，即不擅长，如果是false那么就删除
    num = 0#定义一个编码，后续用于匹配分段后的序号
    downloadFileName = "test.jpg"#定义文件名
    f = open(downloadFileName, "wb")
    while True:
        # 接收服务发送回来的应答数据
        responseData = udpSocket.recvfrom(1024)
        #print(responseData)
        #应答数据结构：数据，地址信息（ip,port）
        recvData, serverInfo = responseData
        #print(recvData)
        #应答数据中数据中有三部分：1、操作码-元组（n,）2、分页页码-元组（n,）3、数据内容
        opNum = struct.unpack("!H", recvData[:2])
        packetNum = struct.unpack("!H", recvData[2:4])
        print("opnum=%s"%opNum)
        print("packetNum=%s"%packetNum)
        if opNum[0] == 3:#操作码为3时，服务器发送过来的是文件的内容
            num += 1
            # 如果一个下载的文件特别大，即接收到的数据包编号超过了2个字节的大小
            # 那么会从0继续开始，所以这里需要判断，如果超过了65535 那么就改为0
            if num == 65536:
                num = 0
            # 判断这次接收到的数据的包编号是否是 上一次的包编号的下一个，packetNum[0]是
            # 如果是才会写入到文件中，否则不能写入（因为会重复）
            if num == packetNum[0]:
                f.write(recvData[4:])
                # 这个语句貌似多此一举，但是如果返回的数据包编号不是从1开始的话还是有用的，
                # 但是如果上游不是1开始的话也执行不到这一句。很矛盾。。。
                num = packetNum[0]
            #整理ack消息，规则就是这样："!HH"表示四个字节
            ackData = struct.pack("!HH", 4, packetNum[0])
            #将ack消息发送到TFTP服务器，服务器地址是从应答数据中提取的
            udpSocket.sendto(ackData, serverInfo)

        elif opNum[0] == 5:#操作码为5时，表示错误
            print("sorry,木有这个文件")
            flag = False#若数据不存在，则flag赋值False，供后续删除文件使用
        # 为了标记数据已经发送完毕，所以规定，当客户端接收到的数据小于516
        # （2字节操作码+2个字节的序号+512字节数据）时，就意味着服务器发送完毕了
        if len(recvData) < 516:
            break

    if flag == True:
        f.close()
    else:
        os.unlink(downloadFileName)

if __name__ == "__main__":
    main()
