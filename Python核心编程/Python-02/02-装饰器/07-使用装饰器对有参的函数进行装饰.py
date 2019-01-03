#装饰无参数函数
def func(functionName):
    print("--func--1--")
    def func_in(a,b):
        print("--func_in--1--")
        functionName(a,b)
        print("--func_in--2--")
    print("--func--2--")
    return func_in

@func
def test(a , b):
    print("--test1--a=%d--b=%d--"%(a,b))

test(1,2)

'''
--func--1--
--func--2--
--func_in--1--
--test1--a=1--b=2--
--func_in--2--
'''