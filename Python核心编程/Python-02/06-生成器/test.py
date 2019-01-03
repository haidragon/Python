'''
#普通方法
def creatNum():
    print("函数---start")
    a,b = 0,1
    for i in range(5):
        print(b)
        a,b = b,a+b
    print("函数---start")
creatNum()
'''
#生成器
def creatNum1():
    print("生成器---start")
    a,b = 0,1
    for i in range(5):
        print("==1==")
        print(b)
        yield(b)
        print("==2==")
        a,b = b,a+b
        print(b)
        print("==3==")
    print("生成器---end")
#创建了一个生成器对象
a = creatNum1()

ret = a.__next__()
print(ret)
#以上两种方式是等价的
next(a)
a.__next__()



'''
while True:
    try :
        b = next(a)
        print(b)
    except StopIteration as e :
        print("生成器返回值%s"%e.value)
        break
'''
