from multiprocessing import Pool
import time
import os

def test():
    print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("-----%d-----"%i)
        time.sleep(1)
    return "haha"

def test2(args):
    print("callback func--pid=%d"%os.getpid())
    print("callback func--args=%s"%args)


if __name__ == "__main__":
    pool = Pool()
    #apply_async(func[, args[, kwds[, callback[, error_callback]]]])
    #如果指定callback，那么它应该是一个可接受单个参数的可调用对象。当结果完成时就对
    #它应用callback，在调用失败的情况下则应用error_callback。
    #如果指定error_callback，那么它应该是一个接受单个参数的可调用对象。
    #如果目标函数失败，则以该异常实例调用error_callback
    #回调应该立即完成，否则处理结果的线程将被阻塞。
    pool.apply_async(func=test,callback=test2)

    while True:
        time.sleep(1)
        print("-----主进程-pid=%d"%os.getpid())