class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("%s在吃"%self.name)

@staticmethod
def printNum():
    print("----staticmethod----")

Person.printNum = printNum
Person.printNum()

@classmethod
def printNum1(cls):
    print("----classmethod----")
Person.printNum1 = printNum1
Person.printNum1()

'''
p = Person("wang",10)
p.printNum = printNum
p.printNum()
-----------------------
TypeError: 'staticmethod' object is not callable
不可将静态方法/类方法添加到对象上面， 静态方法属于类，应该添加到类上面。 Person.xy=test，这样Person类的所有对象都会自动拥有xy属性
'''