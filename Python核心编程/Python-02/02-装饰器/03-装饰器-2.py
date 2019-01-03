def w1(func):
    def inner():
        print("校验")
    return inner

@w1
def f1():
    print("--f1--")
def f2():
    print("--f2--")
def f3():
    print("--f3--")
def f4():
    print("--f4--")

f1()



