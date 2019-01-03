#1、打印功能提示
print("="*50)
print("名片管理系统")
print("1：添加")
print("2：删")
print("3：改")
print("4：查")
print("5：显示全部")
print("6：退出")
print("="*50)
#定义一个列表，用来存储用户（字典），类似java的List用来存储Object
card_info = []
while True:
    # 2、获取用户输入

    tempIn = input("请输入功能序号")
    if tempIn == "":
        print("输入了空值")
    else:
        num = int(tempIn)
        #3、根据用户数据执行相应的功能
        if num == 1:
            new_name = input("请输入用户名")
            new_qq = input("请输入qq")
            new_weixin = input("请输入微信")
            new_addr = input("请输入地址")
            #创建一个字典，用于存储用户信息
            new_info = {}
            new_info["name"] = new_name
            new_info["qq"] = new_qq
            new_info["weixin"] = new_weixin
            new_info["addr"] = new_addr
            #将字典存储到列表中
            card_info.append(new_info)
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            search_name = input("请输入需要查询的用户名")
            find_flag = 0 #0表示未查询到对应用户
            #遍历card_info列表，取出所有的用户
            for temp in card_info:
                #判断输入的用户名是否在列表中的字典用户信息中
                if search_name == temp.get("name"):
                    print("姓名\t微信\tQQ\t住址")
                    print("%s\t%s\t%s\t%s" % (temp["name"], temp["weixin"], temp["qq"], temp["addr"]))
                    #查询到对应数据时，将查询状态设置为1：已查询到
                    find_flag = 1
                    #查询到数据后结束循环（此处操作不太完善，但是和程序结构无关只是业务层面会有BUG）
                    break
            if find_flag == 0:
                    print("信息不存在")
        elif num == 5:
            print("姓名\t微信\tQQ\t住址")
            for temp in card_info:
                print("%s\t%s\t%s\t%s"%(temp["name"],temp["weixin"],temp["qq"],temp["addr"]))
        elif num == 6:
            break
        else:
            print("输入有误")
        print(card_info)



