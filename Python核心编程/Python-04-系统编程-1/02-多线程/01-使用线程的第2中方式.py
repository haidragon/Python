from threading import Thread
import time

class MyThread(Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            print("I'm " + self.name + " @ " + str(i))#name中的属性是当前线程的名字

if __name__ == "__main__":
    t = MyThread()
    t.start()

'''I'm Thread-1 @ 0
I'm Thread-1 @ 1
I'm Thread-1 @ 2
I'm Thread-1 @ 3
I'm Thread-1 @ 4'''