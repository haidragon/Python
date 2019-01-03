class Store(object):
    def select_car(self):
        pass
    def order(self,car_type):
        return self.select_car(car_type)
class BMWFactory(object):
    def select_car_by_type(self,car_type):
        if car_type == "720":
            car = BMW720()
        elif car_type == "750":
            car = BMW750()
        return car

class BMWStrore(Store):
    def select_car(self,car_type):
        return BMWFactory().select_car_by_type(car_type)


class CarStore(Store):
    def select_car(self,car_type):
        return Factory().select_car_by_type(car_type)

class Factory(object):
    def select_car_by_type(self,car_type):
        if car_type == "伊兰特":
            car = YilanteCar()
        elif car_type == "索纳塔":
            car = SuonataCar()
        return car

class Car(object):
    def move(self):
        print("----车在移动----")
    def stop(self):
        print("----停车----")

class YilanteCar(Car):
    def __str__(self):
        return "YilanteCar"

class SuonataCar(Car):
    def __str__(self):
        return "SuonataCar"

class BMW720(Car):
    def __str__(self):
        return "BMW720"
class BMW750(Car):
    def __str__(self):
        return "BMW750"

'''car_store = CarStore()
car = car_store.order("索纳塔")
print(car)
car.move()'''



bmw_car_store = BMWStrore()
bmw_car = bmw_car_store.order("720")
print(bmw_car)
bmw_car.move()