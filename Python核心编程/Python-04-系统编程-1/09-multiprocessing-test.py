from multiprocessing import Process
import os
import time
#⼦进程要执⾏的代码
def son(name1,name2):
    print("子进程正在运行，name1 = %s,name2 = %s,pid = %d" %(name1,name2,os.getpid()))
    time.sleep(0.5)
def run(name1,name2):
    print("子进程run正在运行，name1 = %s,name2 = %s,pid = %d" % (name1, name2, os.getpid()))



if __name__ == "__main__":
    #创建一个Process的对象，并将要执行的对象和对象的参数传入进去
    p = Process(target=son,args=("名字1","名字2",))
    print("⽗进程 %d." % os.getpid())
    print("⼦进程将要执⾏")
    p.start()#通过p.start()方法创建子进程
    time.sleep(1)
    p.terminate()
    p.join()#等待子进程结束后再往下运行，不然可能会出现下面的语句先执行完毕子进程再执行的情况
    print("⼦进程已结束")


"""
创建⼦进程时，只需要传⼊⼀个执⾏函数和函数的参数，创建⼀个Process实例，⽤start()⽅法启动，这样创建进程⽐fork()还要简单。
join()⽅法可以等待⼦进程结束后再继续往下运⾏，通常⽤于进程间的同步。
"""