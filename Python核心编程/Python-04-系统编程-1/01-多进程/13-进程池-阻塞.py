from multiprocessing import Pool
import time
import os
import random

def work(msg):
    t_startTime = time.time()
    print("%s进程正在运行，进程ID=%s"%(msg,os.getpid()))
    time.sleep(random.random()*2.125)
    t_endTime = time.time()
    print("%s执行完毕，耗时%d"%(msg,t_endTime-t_startTime))

if __name__ == "__main__":
    po = Pool()
    for i in range(10):
        po.apply(work,(i,))#Pool.apply_async(要调⽤的⽬标,(传递给⽬标的参数元祖,))每次循环将会⽤空闲出来的⼦进程去调⽤⽬标
    print("-----start-----")
    po.close()#关闭进程池，关闭后po不再接收新的请求
    po.join() #等待po中所有⼦进程执⾏完成，必须放在close语句之后,否则会报错
    print("-----end-----")

'''0进程正在运行，进程ID=138784
0执行完毕，耗时0
1进程正在运行，进程ID=143308
1执行完毕，耗时1
2进程正在运行，进程ID=115740
2执行完毕，耗时1
3进程正在运行，进程ID=124996
3执行完毕，耗时1
4进程正在运行，进程ID=138784
4执行完毕，耗时1
5进程正在运行，进程ID=143308
5执行完毕，耗时0
6进程正在运行，进程ID=115740
6执行完毕，耗时0
7进程正在运行，进程ID=124996
7执行完毕，耗时1
8进程正在运行，进程ID=138784
8执行完毕，耗时0
9进程正在运行，进程ID=143308
9执行完毕，耗时0
-----start-----
-----end-----'''
