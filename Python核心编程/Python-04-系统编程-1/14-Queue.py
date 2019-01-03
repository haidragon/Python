from multiprocessing import Pool
from multiprocessing import Manager
import os
import time
import random

def work1(queue1):
    print("开始执行-1，进程ID=%s"%os.getpid())
    for i in "dogge1":
        if not queue1.full():
            queue1.put(i)
            time.sleep(2)
        else:
            print("queue1满了")
    print("执行完毕-1，进程ID=%s"%os.getpid())

def work2(queue2):
    stat = False
    print("开始执行-2，进程ID=%s"%os.getpid())
    t_startTime = time.time()
    while True:
        if not queue2.empty():
            for i in range(queue2.qsize()):
                q_msg = queue2.get()
                print("q_msg=%s"%q_msg)
                time.sleep(1)
                if str(q_msg) == "1":
                    stat = True
                    break
        if stat:
            break
    t_endTime = time.time()
    print("执行完毕-2，进程ID=%s,耗时%s"%(os.getpid(),t_endTime - t_startTime))


if __name__ == "__main__":
    q = Manager().Queue()
    po = Pool(4)
    po.apply_async(work1,(q,))
    po.apply_async(work2,(q,))
    #po.apply_async(work,(i,))
    print("----start----")
    po.close()
    po.join()
    print("----end----")
