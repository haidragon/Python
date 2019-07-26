#1.了解内置函数的使用，并给出一个调用示例（library.pdf – 内置函数）
#abs()	all()	min()	any()	hex()	str()	ord()
def u_abs():
    a = -100
    print(abs(a))

#2.1-100之间的偶数进行累加，并打印出计算结果（使用continue）
def u_even():
    sum = 0
    for i in range(1,101):
        if i % 2 == 0 :
            sum = sum + i
        else:
            continue
    print(sum)

#3.打印1-100之间的奇数并且能被3整除
def u_odd():
    sum = 0
    for i in range(1,101):
        if i % 2 == 0 :
            continue
        elif i % 3 == 0:
            sum = sum + i
    print(sum)


#4.遍历字符串”hello world”，如果遇到l不打印 ,遇到w退出循环
def u_hello():
    s = "hello world"
    for i in s:
        if i == "l":
            continue
        elif i == "w":
            break
        else:
            print(i)

#5.遍历字符串”abcdefghijk”，如果遇到下标是偶数不打印
def u_str():
    s = "abcdefghijk"
    for i in range(0,len(s)):
        if i % 2 != 0:
            print("i=%d时，s[%d]=%s"%(i,i,s[i]))

#6.打印乘法口诀表
def u_multiplication():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d×%d=%d\t"%(j,i,i*j),end="")
        print()

#7.用户登录系统：将几组不同的用户名和密码数据预先预存到List中（列表和字典嵌套使用），
# 使用input()函数让用户输入用户名和密码，然后通过遍历来判断用户名和密码是否匹配，
# 并将登录结果打印出来（登录成功、用户不存在、密码错误）
def u_login():
    u_map = {}
    while True:
        a = int(input("请选择操作：1、注册\t2、删除\t3、登录\t4、退出\n"))
        if a == 1:
            username = input("用户名：")
            password = input("密码：")
            u_map[username] = password
            print(u_map)
        if a == 2:
            username = input("要删除的用户名")
            try:
                u_map.pop(username)
                print(u_map)
            except Exception as e:
                print("用户不存在")
        if a == 3:
            username = input("要登录的用户名")
            password = input("密码")
            try:
                u_password = u_map[username]
                if u_password == password:
                    print("登录成功")
                else:
                    print("密码不匹配")
            except Exception as e:
                print("用户名不存在")
                print(e)
        if a == 4:
            exit(0)

def u_login2():
    list = []
    while True:
        try:
            a = 9999
            a = int(input("请选择操作：1、注册\t2、删除\t3、登录\t4、退出\n"))
            if a == 1:
                username = input("用户名")
                password = input("密码")
                u_map = {}
                u_map[username] = password
                print(u_map)
                statu = False
                if len(list) > 0:
                    for i in range(len(list)):
                        if username in list[i]:
                            print("用户已存在，覆盖原密码")
                            list[i][username] = password
                            statu = True
                    if statu:
                        pass
                    else:
                        print("1-用户不存在，新增。。。")
                        list.append(u_map)
                else:
                    print("2-用户不存在，新增。。。")
                    list.append(u_map)
                print(list)


            elif a == 2:
                username = input("用户名")
                statu = False
                for i in range(len(list)):
                    if username in list[i]:
                        print("用户已存在，删除。。。。。")
                        list.remove(list[i])
                        statu = True
                if statu:
                    pass
                else:
                    print("用户不存在")
                print(list)

            elif a == 3:
                username = input("用户名")
                password = input("密码")
                statu = False
                for i in list:
                    if username in i:
                        statu = True
                        if i[username] == password:
                            print("登录成功")
                        else:
                            print("密码错误")
                if statu:
                    pass
                else:
                    print("用户不存在")
            elif a == 4:
                exit(0)
        except Exception as e:
            print("请输入1-4的数字")


def u_collection():
    strong = {'张飞', '关羽', '赵云', '吕布', '张辽', '周瑜'}
    smart = {'诸葛亮', '周瑜', '赵云', '庞统', '张辽', '荀彧', '郭嘉', '关羽'}

    #1)打印出文武双全的人物
    print(strong&smart)
    #2)打印出武艺超群，但是智商不在线的人物
    print(strong - smart)
    #3)打印出高智商，但是武力较差的人物
    print(smart - strong)
    #4)打印出所有人物，不能重复
    print(strong | smart)

if __name__ == "__main__":
    u_multiplication()