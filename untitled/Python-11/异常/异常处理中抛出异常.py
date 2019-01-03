class Test(object):
    def __init__(self,switch):
        self.switch = switch
    def calc(self,a,b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print("捕获开启，也已经捕获到异常，信息如下")
                print(result)
