
def func(num):
    list = [i for i in range(num)]
    for i in range(num):
        if i == 0 or i ==1:
            list[i] = 1
        else:
            list[i] = list[i-1] + list[i-2]

    return list,list[num-1]

def func2(num):
    a = 0
    b = 1
    while b <= 1000:
        print(b)
        temp = b
        b = a + b
        a = temp
        #a,b = b, a+b


if __name__ == '__main__':
    num = int(input("请输入计算次数\n"))
    list,end = func(num)
    print(list)
    print(end)

    #func2(num)