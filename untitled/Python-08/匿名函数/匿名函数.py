#定义普通函数
def test(x, y):
    x + y
#调用普通函数
result1 = test(11, 22)
print("result1=%s" % result1)

#定义匿名函数
func = lambda a, b: a + b
#调用匿名函数
result2 = func(11, 22)
print("result2=%s" % result2)

'''
result1=None
result2=33
'''
