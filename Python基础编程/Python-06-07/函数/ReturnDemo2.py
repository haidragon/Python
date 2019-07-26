def test():
    a = 11
    b = 22
    c = 33
    # 第一种：列表
    return [a, b, c]
    # 第二种：字典
    return {a, b, c}
    #第三种：元组
    return (a, b, c)
    #第四种:相当于被封装为元组返回
    return  a,b,c
num = test()
print(num)
