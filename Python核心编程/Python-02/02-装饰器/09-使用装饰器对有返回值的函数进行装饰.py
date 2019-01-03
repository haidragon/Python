#装饰有返回值的函数
def func(functionName):
    print("--func--1--")
    def func_in(*args,**kwargs):
        print("--func_in--1--")
        ret = functionName(*args,**kwargs)
        print("--func_in--2--")
        #装饰有返回值的函数，需要接收返回值之后再将返回值返回即可
        return ret
    print("--func--2--")
    return func_in

@func
def test(a , b , c):
    print("--test1--a=%d--b=%d--c=%d--"%(a,b,c))
    return (a+b+c)

@func
def test2(a , b , c , d):
    print("--test1--a=%d--b=%d--c=%d--d=%d"%(a,b,c,d))

print(test(1,2,4))


'''
--func--1--
--func--2--
--func--1--
--func--2--
--func_in--1--
--test1--a=1--b=2--c=4--
--func_in--2--
7
'''