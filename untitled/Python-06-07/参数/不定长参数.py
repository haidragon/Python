#"*args"即为不定长参数，超出参数数量的实参都会传递给args，args为元组
def test(a,b,*args):
    print("a=%d"%a)
    print("b=%d" % b)
    print(args)

test(11,22,33)
'''
执行结果
a=11
b=22
(33,)'''

test(11,22)
'''
执行结果
a=11
b=22
()
'''

#操作不定长参数所有输入值
def test2(a,b,*args):
    result = a+b
    for i in args:
        result = result + i
    print("result=%d"%result)

test2(11,22,33,44,55,66)

'''执行结果：result=231'''