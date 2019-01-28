from threading import Thread,Lock

g_num = 0

def test1():
    global g_num
    #加锁
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    #解锁
    mutex.release()
    print("---in test1,g_num is %d---"%g_num)

def test2():
    global g_num
    #两个线程都抢着对这个锁进程上锁，如果一方成功上锁，那么导致另外的一放歌堵塞，直到这个锁被解开
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    #解锁
    mutex.release()
    print("---in test2,g_num is %d---"%g_num)

#创建一个互斥锁，默认未上锁
mutex = Lock()

p2 = Thread(target=test2)
p2.start()

p1 = Thread(target=test1)
p1.start()





