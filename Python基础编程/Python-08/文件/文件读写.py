#1、打开文件
f = open("D:/Personal/Desktop/test.txt","w")
#2、写入数据
f.write("hello world")
#3、关闭文件
f.close()


f = open('D:/Personal/Desktop/test.txt', 'r')

content = f.read(5)

print(content)

print("-"*30)

content = f.read()

print(content)

f.close()