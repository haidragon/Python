import sys
class T:
    pass

t = T()
t1 = t
t2 = T()

print(sys.getrefcount(t))