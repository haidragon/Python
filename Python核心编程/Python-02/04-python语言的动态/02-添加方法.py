import types

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("%s在吃"%self.name)

p1 = Person("p1",10)
print(p1.name)

def run(self):
    print("%s在跑"%self.name)

#接收的参数是无意义的，在types.MethodType(run,p1)时，方法中的self已经被确定了
p1.run = types.MethodType(run,p1)
p1.run()
#xxx和p1.run都只是用来找到types.MethodType(run,p1)所创建的函数的引用而已
xxx = types.MethodType(run,p1)
xxx()




