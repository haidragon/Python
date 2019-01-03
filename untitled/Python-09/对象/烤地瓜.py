class SweetPotato:
    #定义初始化方法
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []
    def __str__(self):
        return "地瓜是%s,佐料有%s"%(self.cookedString,str(self.condiments))
    def cook(self,time):
        self.cookedLevel += time

        if self.cookedLevel > 8:
            self.cookedString = "烤成灰了"
        elif self.cookedLevel > 5:
            self.cookedString = "熟了"
        elif self.cookedLevel > 3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"
    def addCondiments(self,Condiments):
        self.condiments.append(Condiments)
Potato = SweetPotato()

Potato.cook(1)
print(Potato)
Potato.cook(1)
print(Potato)
Potato.cook(1)
print(Potato)
Potato.cook(1)
print(Potato)
Potato.cook(1)
print(Potato)
print("="*20)
Potato.cook(1)
Potato.addCondiments("ilo")
print(Potato)
Potato.cook(1)
print(Potato)
