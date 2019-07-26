class Person(object):
    def __init__(self,arg):
        super(Person,self).__init__()
        self.name = name

class Gun(object):
    '''枪类'''
    def __init__(self):
        super(Gun,self).__init__()
        self.name = name #记录枪的类型

class Danjia(object):
    '''弹夹类'''
    def __init__(self,max_num):
        super(Danjia,self).__init__()
        self.max_num = max_num
class Zidan(object):
    def __init__(self,arg):
        super(Zidan,self).__init__()
        self.arg = arg


def mian():
'''用来控制整个程序的流程'''

#1、创建老王对象
laowang = Person("老王")
#2、创建枪对象
ak47 = Gun("AK47")
#3、创建一个弹夹对象
dan_jia = Danjia(20)
#4、创建一些子弹
zi_dan = Zidan()
#5、创建一个敌人

#6、把子弹安装到弹夹中
laowang.anzhuang_zidan(dan_jia,zi_dan)
#7、把弹夹安装到枪中
#8、拿枪
#8、开枪

if __name__ == 'main':
    main()