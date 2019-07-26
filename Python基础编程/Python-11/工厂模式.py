# 定义伊兰特车类
class car(object):
    def __str__(self):
        return "制造了一辆"+self.typeName
    def move(self):
        print("---车在移动---")
    def stop(self):
        print("---停车---")
class YilanteCar(car):
    typeName = "伊兰特"
    pass
# 定义索纳塔车类
class SuonataCar(car):
    typeName = "索纳塔"
    pass
# 定义一个生产汽车的工厂，让其根据具体的订单生产车
class CarFactory(object):
    def createCar(self,typeNme):
        if typeNme == "伊兰特":
            car = YilanteCar()
        elif typeNme == "索纳塔":
            car = SuonataCar()
        return car
# 定义一个销售北京现代车的店类
class CarStore(object):
    #设置4s店的指定生产汽车的工厂
    def __init__(self):
        self.carfactory = CarFactory()
    def order(self,typeName):
        car = self.carfactory.createCar(typeName)
        print(car)

carstore = CarStore()
carstore.order("索纳塔")