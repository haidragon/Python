from threading import Thread
import time

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("---in test1,g_num is %d---"%g_num)


def test2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("---in test2,g_num is %d---"%g_num)

p1 = Thread(target=test1)
p1.start()

#time.sleep(2),不slee时，数值不对
'''---in test1,g_num is 1127198---
---in test2,g_num is 1254476---'''
p2 = Thread(target=test2)
p2.start()



