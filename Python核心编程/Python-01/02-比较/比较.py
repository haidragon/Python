a = [11,22,33]
b = [11,22,33]
c = a
print("id(a)=%s"%id(a))
print("id(b)=%s"%id(b))
print("id(c)=%s"%id(c))
#==判断内容是否相同
print(a == b)#True
#is：判断内存地址是否相同
print(a is b)#False
print(a is c)#True

print("="*20)
d = 127
e = 127
print(d == e)#True
print(d is e)#True

print("="*20)
f = 13000
g = 13000
print(f == g)#True
print(f is g)#True

