import functools
def showarg(*args, **kw):
    print(args)
    print(kw)
    print("=")

p1=functools.partial(showarg, 1,2,3)
p1()
'''(1, 2, 3)
{}'''

p1(4,5,6)
'''(1, 2, 3, 4, 5, 6)
{}'''
p1(a='python', b='itcast')
'''(1, 2, 3)
{'a': 'python', 'b': 'itcast'}'''
p2=functools.partial(showarg, a=3,b='linux')
p2()
'''()
{'a': 3, 'b': 'linux'}'''
p2(1,2)
'''(1, 2)
{'a': 3, 'b': 'linux'}'''
p2(a='python', b='itcast')
'''()
{'a': 'python', 'b': 'itcast'}'''