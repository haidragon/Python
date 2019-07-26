class Dog:
    #私有方法
    def __send_msg(self):
        print("---正在发送短信----")
    #公有方法
    def send_msg(self,money):
        if money > 1000:
            #私有方法只能在类中调用
            self.__send_msg()
        else:
            print("余额不足")
class D(Dog):
    #公有方法
    def send_msg(self,money):
        if money > 2000:
            #私有方法只能在类中调用
            self.__send_msg()
        else:
            print("余额不足")

class E(D):
    pass



dog = E()
#@dog.__send_msg()#调用会失败

dog.send_msg(1500)