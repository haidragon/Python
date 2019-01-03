#创建一个类
class cat:
    #属性
    #方法
    def __init__(self,a,b):
        self.name = a
        self.age = b
    def __str__(self):
        return "--str--"
    def eat(self):
        print("猫在吃饭")
    def drink(self):
        print("猫在喝水")
    #若需要创建多个对象都调用这个方法，则形参需要都为self
    def introduce(self):
        print("%s的年龄为%d"%(self.name,self.age))
#创建一个对象
tom = cat("汤姆",40)

#调用类中的方法
tom.drink()
tom.eat()
#添加属性
#tom.name = "汤姆"
#tom.age = 40
#调用自我介绍方法
tom.introduce()

#定义第二个类
lanmao = cat("蓝猫",20)
#lanmao.name = "蓝猫"
#lanmao.age = 20
lanmao.introduce()

#定义第三个类
jumao = cat("橘猫",10)
print(jumao)