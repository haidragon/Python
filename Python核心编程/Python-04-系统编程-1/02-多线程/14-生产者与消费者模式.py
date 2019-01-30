from threading import Thread
from multiprocessing import Queue
import time


class Producer(Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                count += 1
                msg = self.name + "生成产品" + str(count)
                queue.put(msg)
                print(msg)
            time.sleep(0.5)

class Consumer(Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + "消费了" + queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == "__main__":
    queue = Queue()

    for i in range(500):
        msg = "初始化数据 " + str(i)
        queue.put(msg)

    for i in range(2):
        p1 = Producer()
        p1.start()
    for i in range(5):
        c1 = Consumer()
        c1.start()



