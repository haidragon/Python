import copy
a = [1,2,3]
b = [4,5,6]
c = (a,b)
e = copy.copy(c)
#元组为不可变类型，copy.copy会判断被拷贝对象是否为可变类型，若为可变类型则拷贝一层，若为非可变类型则，则直接就是浅拷贝
print("id(e)=%s"%id(e))#id(e)=3117827726024
print("id(c)=%s"%id(c))#id(c)=3117827726024




