class ShortInputException(Exception):
    #自定义异常类需要继承Exception类
    def __init__(self, length, atleast):
        super.__init__()
        self.length = length
        self.atleast = atleast

def main():
    s = input("请输入")
    try:
        if len(s) < 3:
            #抛出异常
            raise ShortInputException(len(s),3)
    except ShortInputException as result:
        print("输入长度为%d,长度至少应该为%d"%(result.length,result.atleast))
    else:
        print("无异常")

main()