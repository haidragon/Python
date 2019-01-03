class A:
    def __init__(self):
        self.num = 100
        self.__num2 = 200
    def test1(self):
        print("--------test1-----------")
    def __test2(self):
        print("--------test2-----------")
    def test3(self):
        self.__test2()
        print(self.__num2)
class B(A):
    pass

b = B()
#b.__test2()#私有方法不会被继承
#print(b.num)
#print(b.__num2)#私有属性不会被继承

b.test3()
print(B.__mro__)