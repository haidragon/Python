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
for i in a:
    print(i)
