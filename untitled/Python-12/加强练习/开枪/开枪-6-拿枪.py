class Person(object):
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name
        self.gun = None#保存枪的引用
        self.hp = 100
    def __str__(self):
        if self.gun:
            return "%s的血量为%d，他有枪"%(self.name,self.hp)
        else:
            return "%s的血量为%d，他没有枪"%(self.name,self.hp)
    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        '''把子弹装到弹夹中'''
        #弹夹.保存子弹
        dan_jia_temp.baocun_zidan(zi_dan_temp)
    def anzhuang_danjia(self,gun_temp,dan_jia_temp):
        '''把弹夹安装到枪中'''
        #枪.保存弹夹（弹夹）
        gun_temp.baocun_danjia(dan_jia_temp)
    def na_qiang(self,gun_temp):
        '''拿起一把枪'''
        self.gun = gun_temp


class Gun(object):
    '''枪类'''
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name = name #记录枪的类型
        self.danjia = None#用来记录弹夹对象的引用
    def __str__(self):
        if self.danjia:
            return "枪的类型：%s,弹夹：%s"%(self.name,self.danjia)
        else:
            return "枪的类型：%s,无弹夹" %(self.name)

    def baocun_danjia(self,dan_jia_temp):
        self.danjia = dan_jia_temp

class Danjia(object):
    '''弹夹类'''
    def __init__(self,max_num):
        super(Danjia,self).__init__()
        self.max_num = max_num#记录弹夹的最大容量
        self.zidan_list = []#记录所有子弹的引用

    def __str__(self):
        return "子弹列表%d/%d"%(len(self.zidan_list),self.max_num)

    def baocun_zidan(self,zi_dan_temp):
        self.zidan_list.append(zi_dan_temp)

class Zidan(object):
    def __init__(self,sha_shang_li):
        super(Zidan,self).__init__()
        self.sha_shang_li = sha_shang_li


def main():
    '''用来控制整个程序的流程'''

    #1、创建老王对象
    laowang = Person("老王")
    #2、创建枪对象
    ak47 = Gun("AK47")
    m14 = Gun("M14")
    #3、创建一个弹夹对象
    dan_jia = Danjia(20)
    #4、创建一些子弹
    for i in range(15):
        zi_dan = Zidan(10)
        #5、把子弹安装到弹夹中
        laowang.anzhuang_zidan(dan_jia,zi_dan)
    #6、把弹夹安装到枪中
    #laowang.安装到枪中(枪,弹夹)
    laowang.anzhuang_danjia(ak47,dan_jia)

    #test1：测试弹夹的信息
    print(dan_jia)
    #test2：测试枪的信息
    print(ak47)
    print(m14)

    #7、拿枪
    laowang.na_qiang(ak47)
    # test3：测试老王的信息
    print(laowang)
    #8、创建一个敌人
    #9、开枪

if __name__ == 'main':
    main()
else:
    main()