#1、打开文件
f = open("D:/Personal/Desktop/test.txt","r")
#2、读取数据
content = f.readlines()
#3、打印返回值类型
print(type(content))
#4、打印返回值内容
i = 0
for temp in content:
    print("i=%d,temp=%s"%(i,temp))
    i += 1
#5、关闭文件
f.close()