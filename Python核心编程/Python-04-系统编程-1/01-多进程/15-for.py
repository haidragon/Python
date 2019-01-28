import time

def test1():
    startTime = time.time()
    for i in range(1,1000):
        for j in range(1,1000):
            for k in range(1,1000):
                time.time()
    endTime = time.time()
    print("耗时%d"%(endTime-startTime))


if __name__ == "__main__":
    test1()