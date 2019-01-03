#装饰不定长参数函数
def func(functionName):
    print("--func--1--")
    def func_in(*args,**kwargs):
        print("--func_in--1--")
        functionName(*args,**kwargs)
        print("--func_in--2--")
    print("--func--2--")
    return func_in

@func
def test(a , b , c):
    print("--test1--a=%d--b=%d--c=%d--"%(a,b,c))

@func
def test2(a , b , c , d):
    print("--test1--a=%d--b=%d--c=%d--d=%d"%(a,b,c,d))

test(1,2,3)
test2(4,5,6,7)

'''
--func--1--
--func--2--
--func--1--
--func--2--
--func_in--1--
--test1--a=1--b=2--c=3--
--func_in--2--
--func_in--1--
--test1--a=4--b=5--c=6--d=7
--func_in--2--
'''