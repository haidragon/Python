class Test(object):
    def __init__(self):
       self.__num = 100
    @property#装饰器，表示下面的方法是get方法，且方法名就是普通property属性名，顺序不能反，get方法要在上
    def num(self):
        print("----getter----")
        return self.__num
    @num.setter#装饰器，表示下面的方法是set方法，且方法名就是普通property属性名
    def num(self, newNum):
        print("----setter----")
        self.__num = newNum
t = Test()
print("-"*50)
t.num = 200 #相当于调用了 t.setNum(200)
print(t.num) #相当于调用了 t.getNum()

#注意点:
#t.num 到底是调用getNum()还是setNum(),要根据实际的场景来判断,
#1. 如果是给t.num赋值 那么一定调用setNum()
#2. 如果是获取t.num的值,那么就一定调用getNum()
#
#property的作用:相当于把方法进行了封装, 开发者在对属性设置数据的时候更方便

