from threading import Thread
import threading
import time

def test1():
    name = threading.current_thread().name
    print("---thread name is %s----"%name)
    g_num = 100
    if name == "Thread-1":
        g_num += 1
    else:
        time.sleep(2)
    print("---thread name is %s----g_num=%d"%(name, g_num))

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test1, name="xxxxxx")
p2.start()

'''---thread name is Thread-1----
---thread name is Thread-1----g_num=101
---thread name is xxxxxx----
---thread name is xxxxxx----g_num=100'''