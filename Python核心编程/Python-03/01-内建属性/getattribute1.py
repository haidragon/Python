class Person:
    def __getattribute__(self, item):
        if item == "a":
            print("haha")
        else:
            return object.__getattribute__(self,"test")

    def test(self):
        print("test")

p = Person()

p.a
p.b