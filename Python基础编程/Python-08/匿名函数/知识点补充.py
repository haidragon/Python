a = 4
b = 5

#方式一
c = 0
c = a
a = b
b = c

print("a=%d,b=%d"%(a,b))

a = 4
b = 5
#方式二
a = a + b
b = a - b
a = a - b
print("a=%d,b=%d"%(a,b))

#方式三
a = 4
b = 5
a,b = b,a
print("a=%d,b=%d"%(a,b))