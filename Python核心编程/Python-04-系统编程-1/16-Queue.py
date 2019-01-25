from multiprocessing import Process
from multiprocessing import Queue
import time
import random

def write(q):
    for i in "abcdefg1":
        print("put %s in queue"%i)
        put_queue(q,i)

def put_queue(q,i):
    if not q.full():
        q.put(i)
        time.sleep(random.random())
    else:
        time.sleep(random.random())
        put_queue(q,i)

def read1(q):
    while True:
        if not q.empty():
            msg = q.get(True)
            print("get %s from queue"%msg)
            time.sleep(random.random())
        else:
            break

def read(q):
    while True:
        if not q.empty():
            for i in range(q.qsize()):
                msg = q.get(True)
                print("get %s from queue" % msg)
                time.sleep(random.random())
        else:
            continue#没想出来怎么退出


if __name__ == "__main__":
    q = Queue(3)
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))

    pw.start()

    pr.start()
    pw.join()
    pr.join()
    print("success")



