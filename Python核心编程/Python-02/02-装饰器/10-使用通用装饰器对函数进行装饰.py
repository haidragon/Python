#装饰有返回值的函数
def func(functionName):
    def func_in(*args,**kwargs):
        print("记录日志")
        ret = functionName(*args,**kwargs)
        #装饰有返回值的函数，需要接收返回值之后再将返回值返回即可
        #通用装饰器：此类写法可以不论返回值有无参数、有无返回值的情况下对函数进行装饰
        return ret
    return func_in

@func
def test():
    print("----test----")
    return "haha"

@func
def test2():
    print("----test2----")

@func
def test3(a):
    print("----test3----a = %d"%a)

ret = test()
print("test return value is %s"%ret)

a = test2()
print("test2 return value is %s"%a)

test3(11)

'''
记录日志
----test----
test return value is haha
记录日志
----test2----
test2 return value is None
记录日志
----test3----a = 11
'''


