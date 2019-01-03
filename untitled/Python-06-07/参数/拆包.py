def test(a,b=22,c=33,*args,**kwargs):

    print("a=%d"%a)
    print("b=%d" % b)
    print("c=%d" % c)
    print(args)
    print(kwargs)

A = (44,55,66)
B = {"name":"laowang","age":18}

test(33,22,11,*A,B)
'''结果
a=33
b=22
c=11
(44, 55, 66, {'age': 18, 'name': 'laowang'})
{}
'''
print("= "*10)
test(33,22,11,*A,**B)

'''结果
a=33
b=22
c=11
(44, 55, 66)
{'age': 18, 'name': 'laowang'}
'''