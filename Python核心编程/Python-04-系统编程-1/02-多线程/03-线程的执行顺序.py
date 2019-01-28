from threading import Thread
import time

class MyThread(Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            print("I'm " + self.name + " @ " + str(i))#name中的属性是当前线程的名字

def test():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == "__main__":
    #执行顺序由操作系统确定
    test()
