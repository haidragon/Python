class people(object):
    country = "china"

    @classmethod
    def classGetCountry(cls):
        return  cls.country
    @classmethod
    def classSetCountry(cls):
        cls.country = "EUR"

    def setCountry(self):
        self.country = "US"

    def getCountry(self):
        return self.country

p = people()
p1 = people()
#示例对象的方法对参数进行操作
print(p1.getCountry())#china
p1.setCountry()#实例对象方法设置参数，并不能改变类的参数值
print("="*20)
print(p1.getCountry())#US
print(people.country)#china
print("="*20)

#类对象的方法对参数进行操作
p.classSetCountry()#类对象方法设置参数，能改变类的参数值，也能改变实例对象的值
print(p.getCountry())#EUR
print("="*20)
print(p.classGetCountry())#EUR
print(p.getCountry())#EUR
print(people.country)#EUR




