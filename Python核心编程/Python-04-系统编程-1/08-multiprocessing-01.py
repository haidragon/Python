from multiprocessing import Process
import os
#⼦进程要执⾏的代码
def run_proc(name):
    print("⼦进程运⾏中，name= %s ,pid=%d..." % (name, os.getpid()))

if __name__=="__main__":
    print("⽗进程 %d." % os.getpid())
    p = Process(target=run_proc, args=("test",))
    print("⼦进程将要执⾏")
    p.start()
    p.join()#等待子进程结束后再往下运行，不然可能会出现下面的语句先执行完毕子进程再执行的情况
    print("⼦进程已结束")

"""
创建⼦进程时，只需要传⼊⼀个执⾏函数和函数的参数，创建⼀个Process实例，⽤start()⽅法启动，这样创建进程⽐fork()还要简单。
join()⽅法可以等待⼦进程结束后再继续往下运⾏，通常⽤于进程间的同步。
"""