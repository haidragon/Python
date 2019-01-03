#先看如何隐藏
class Foo:
    __N=111111 #_Foo__N  声明的隐藏属性
    def __init__(self,name):
        self.__Name=name #self._Foo__Name=name

    def __f1(self): #_Foo__f1
        print('f1')
    def f2(self):
        self.__f1() #self._Foo__f1()

f=Foo('egon')#这种是调不到的
print(f.__N)
f.__f1()#这种是调不到的
f.__Name
f.f2()

#1：这种隐藏只是一种语法上变形操作，并不会将属性真正隐藏起来
print(Foo.__dict__)
print(f.__dict__)
print(f._Foo__Name)
print(f._Foo__N)

#2:这种语法级别的变形，是在类定义阶段发生的，并且只在类定义阶段发生
Foo.__x=123123123123123123123123123123123123123123
print(Foo.__dict__)
print(Foo.__x)
f.__x=123123123
print(f.__dict__)
print(f.__x)

#3:在子类定义的__x不会覆盖在父类定义的__x，因为子类中变形成了：_子类名__x,而父类中变形成了：_父类名__x，即双下滑线开头的属性在继承给子类时，子类是无法覆盖的。
class Foo:
    def __f1(self): #_Foo__f1
        print('Foo.f1')

    def f2(self):
        self.__f1() #self._Foo_f1

class Bar(Foo):
    def __f1(self): #_Bar__f1
        print('Bar.f1')

b=Bar()
b.f2()