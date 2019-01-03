# 定义一个基本的4S店类
class Car(object):
    #def setTypeName(self,TypeName):
    #    self.TypeName = TypeName
    def __str__(self):
        return "制造了一台"+self.typeName
    def move(self):
        print("----车在移动----")
    def stop(self):
        print("----停车----")
# 定义伊兰特车类
#class YilanteCar(object):
# 定义车的方法
# 定义索纳塔车类
#class SuonataCar(object):
# 定义车的方法

# 定义一个生产汽车的工厂，让其根据具体得订单生产车
class CarFactory(object):
    def createCar(self,typeName):
        self.car = Car()
        self.car.typeName = typeName
        return self.car

# 定义一个北京现代4S店类
class CarStore(object):
    def __init__(self):
        self.carFactory = CarFactory()
    def __str__(self):
        return "这是一家"+self.storeType+"4S店"
    def setStoreType(self,storeType):
        self.storeType = storeType
    def createCar(self, typeName):
        self.car = self.carFactory.createCar(typeName)
        return self.car
    def order(self, typeName):
        # 让工厂根据类型，生产一辆汽车
        print()
        car = self.createCar(typeName)
        car.move()
        car.stop()
        print(car)


suonata = CarStore()
suonata.setStoreType("现代")
suonata.order("索纳塔")
print(suonata)