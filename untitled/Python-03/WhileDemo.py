#导入随机数工具包
import random
#1.提示并获取用户输入
people = int(input("请输入0：剪刀 1：石头 2：布"))
#2、调用random中的randint生成0-2之间的随机数
computer = random.randint(0,2)
#3、判断用户输入，然后显示对应结果
if (people == 0 and computer == 1) or (people == 1 and computer == 2) or (people == 2 and computer == 0) :
    print("电脑赢了电脑%d人类%d\t"%(computer,people))
elif people == computer:
    print("平局")
else :
    print("人类赢了电脑%d人类%d\t" % (computer, people))







