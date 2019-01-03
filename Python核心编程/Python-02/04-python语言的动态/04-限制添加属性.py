class Person():
    __slots__ = ("name","age")
    def eat(self):
        print("%s在吃"%self.name)

p = Person()

p.age = 10
p.name = "wang"
#只能添加__slots__中定义的内容
#p.addr = "beijing"

print(p.age)