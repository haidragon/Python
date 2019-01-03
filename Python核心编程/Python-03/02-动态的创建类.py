#无父类
def printNum(self):
    print("---num-%d---"%self.num)
Test3 = type("Test3",(),{"printNum":printNum,"num":0}
t1 = Test3()
#t1.num = 100
t1.printNum()
#---num-0---

#有父类
class Animal():
    def cat(self):
        print("--eat--")
Cat = type("Cat",(Animal,),{"printNum":printNum})
cat = Cat()
cat.cat()
#--eat--