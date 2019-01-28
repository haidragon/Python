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
        po.apply_async(work,(i,))#Pool.apply_async(要调⽤的⽬标,(传递给⽬标的参数元祖,))每次循环将会⽤空闲出来的⼦进程去调⽤⽬标
    print("-----start-----")
    po.close()#关闭进程池，关闭后po不再接收新的请求
    po.join() #等待po中所有⼦进程执⾏完成，必须放在close语句之后,否则会报错
    print("-----end-----")

'''-----start-----
0进程正在运行，进程ID=142516
1进程正在运行，进程ID=115740
2进程正在运行，进程ID=128892
3进程正在运行，进程ID=143848
2执行完毕，耗时0
4进程正在运行，进程ID=128892
0执行完毕，耗时0
5进程正在运行，进程ID=142516
5执行完毕，耗时0
6进程正在运行，进程ID=142516
3执行完毕，耗时1
7进程正在运行，进程ID=143848
7执行完毕，耗时0
8进程正在运行，进程ID=143848
1执行完毕，耗时1
9进程正在运行，进程ID=115740
9执行完毕，耗时0
4执行完毕，耗时1
6执行完毕，耗时1
8执行完毕，耗时1
-----end-----'''
