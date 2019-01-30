from threading import Thread

def deadLoop():
    while True:
        pass

if __name__ == "__main__":
    for i in range(7):
        t = Thread(target=deadLoop)
        t.start()

deadLoop()
