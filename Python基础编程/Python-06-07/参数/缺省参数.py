#b和c为缺省参数
def test(a,b=22,c=33):

    print("a=%d"%a)
    print("b=%d" % b)
    print("c=%d" % c)

#c=11为命名参数
test(33,c=11)
'''
执行结果
a=33
b=22
c=11
'''
test(33,11)
'''
执行结果
a=33
b=11
c=33
'''
