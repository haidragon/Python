def test(a, b):
    aa = a
    bb = b
    return aa, bb

#a1/a2分别接收返回值，每个变量存储其中一个值
a1, a2 = test(1, 2)

print("a1=%d" % a1)
print("a2=%d" % a2)
