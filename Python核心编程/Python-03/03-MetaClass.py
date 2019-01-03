#-*- coding:utf-8 -*-
def upper_attr(future_class_name, future_class_parents, future_class_attr):
#遍历属性字典，把不是__开头的属性名字变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            #将属性字典中的属性全部转换为大写再进行赋值
            newAttr[name.upper()] = value
            #调用type使用新的属性来创建一个类
    return type(future_class_name, future_class_parents, newAttr)

class Foo(object, metaclass=upper_attr):
    bar = 'bip'

#此时调用的Foo类就是type创建出来的类，而不是在上一步创建出来的
print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
f = Foo()
print(f.BAR)