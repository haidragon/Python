#打印功能提示
print("="*50)
print("名字管理系统")
print("1：添加")
print("2：删")
print("3：改")
print("4：查")
print("="*50)
#获取用户选择
names = []
#设置程序无限循环，使用户可以连续操作
while True:
    num = int(input("请输入功能序号"))
    #根据用户的选择执行相应的功能
    if num == 1:
        temp = input("请输入需要添加的人名")
        if temp in names:
            print("重名")
        else:
            names.append(temp)
    elif num == 2:
        print("列表内容为：%s"%names)
        print("1：删除指定索引位置的名字")
        print("1：删除指定名称名字")
        num2 = int(input("请输入功能序号(删除)"))
        length = len(names)
        if num2 == 1:
            index = int(input("请输入索引位置"))
            if index >= length:
                print("索引超出列表长度，列表总长度为%d" % length)
            elif index < -length:
                print("索引超出列表长度，列表总长度为%d" % -length)
            else:
                del names[index]
        elif num2 == 2:
            pass
        else:
            pass

    elif num == 3:
        pass
    elif num == 4:
        pass
    elif num == 0:
        break
    else:
        print("输入有误")
    print("name的内容为")
    print(names)