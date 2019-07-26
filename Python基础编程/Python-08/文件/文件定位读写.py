f = open("D:/Personal/Desktop/test.txt",'rb')
#读取3个字节
f.read(3)
print(f.tell())

#在读取3个字节的基础上再读取2个字节
f.read(2)
print(f.tell())

#将读取位置重新定位到开头第二个字节
f.seek(2,0)
print(f.tell())
#从第三个字节开始读取3个字节
temp = f.read(3)
print(temp)
print(f.tell())

#将读取位置重新定位到结尾前第三个字节
f.seek(-3,2)
print(f.tell())
#从第三个字节开始读取3个字节
temp = f.read()
print(temp)
print(f.tell())


