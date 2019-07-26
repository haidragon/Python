#定义一个全局变量
wendu = 0

def getWendu():
    #使用global声明一个全局变量，
    # 此时函数内的wendu就编变成了一个全局变量，
    # 对温度的修改就会影响到函数外的全局变量，
    # 否则对变量wendu的修改只是局部变量发生了变化
    global wendu
    wendu = 33

def printWendu():
    print("温度为%d"%wendu)

getWendu()
printWendu()