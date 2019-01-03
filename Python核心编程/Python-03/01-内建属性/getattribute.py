class Itcast(object):
    def __init__(self,obj1):
        self.subject1 = obj1
        self.subject2 = "cpp"

    #属性访问拦截器
    def __getattribute__(self, obj):
        print("====1>%s"%obj)
        if obj == "subject1":
            print("log subject1")
            return 'redirect python'
            #return object.__getattribute__(self,obj)
        else:
            #如果不想拦截属性，则按照如下填写，将属性传给object的__getattribute__方法即可
            temp = object.__getattribute__(self, obj)
            print("===2>%s"%str(temp))
            return temp

    def show(self):
        print("this is Itcast")

s = Itcast("python")
#此时对象s有两个属性，一个是subject1="python"，一个是subject2="cpp"

#一下为访问s的两个属性
print(s.subject1)
print(s.subject2)

#调用方法和访问属性时的过程是一样的，都要经过__getattribute__方法
s.show()
'''====1>subject1
log subject1
redirect python
====1>subject2
===2>cpp
cpp
====1>show
===2><bound method Itcast.show of <__main__.Itcast object at 0x000002A7EFE47C88>>
this is Itcast'''