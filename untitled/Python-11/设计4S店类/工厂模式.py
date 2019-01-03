class CarStore(object):
    def order(self,car_type):
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

car_store = CarStore()
car = car_store.order("索纳塔")
print(car)
car.move()