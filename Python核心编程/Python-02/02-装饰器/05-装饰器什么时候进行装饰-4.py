def w1(func):
    print("--装饰1--")
    def inner():
        print("校验1")
        func()
    return inner
def w2(func):
    print("--装饰2--")
    def inner():
        print("校验2")
        func()
    return inner
@w1
@w2
def f1():
    print("--f1--")

f1()

'''
饰器-4.py
--装饰2--
--装饰1--
校验1
校验2
--f1--
'''

