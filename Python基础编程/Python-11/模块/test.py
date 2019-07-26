def add(a,b):
    return a + b

ret = add(1,2)
print("int test.py file,,,,1+2=,方法来自%s"%__name__)
'''
直接执行：
int test.py file,,,,1+2=,方法来自main
被引入执行
int test.py file,,,,1+2=,方法来自test
'''