#带有参数的装饰器
def func_arg(arg):
    def func(functionName):
        def func_in():
            print("----记录日志----%s"%arg)
            functionName(arg)
        return func_in
    return func

#带有参数的装饰器
'''
1、先执行func_arg("heihei"),这个函数return的结果是func这个函数的引用
2、此时这个位置就相当于@func
3、使用@func对test进行装饰
'''
@func_arg("heihei")
def test(a):
    print("----test----%s"%a)
#带参数装饰的话，可以在调用带参数的函数时不传参数
test()

'''
----记录日志----heihei
----test----heihei
'''

