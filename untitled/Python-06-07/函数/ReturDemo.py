def getWendu():
    wendu = 22
    print("当前温度为%d" % wendu)
    return wendu


def getWenduHuashi(wendu):
    wendu = wendu + 3
    print("当前温度（华氏）为%d" % wendu)


result = getWendu()
getWenduHuashi(result)
