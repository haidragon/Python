class Dog(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

dog1 = Dog()
print(id(dog1))
dog2 = Dog()
print(id(dog2))

