import re
# 1、打开文件
f = open("D:/Personal/Desktop/Source.txt", "r")
#读取映射表
dic = open("D:/Personal/Desktop/dic.txt", "r")
data = open("D:/Personal/Desktop/data.txt", "w")
str = ""
dict = {}
for line in dic:
    key,value = line.strip().split(":")
    #key = ";" + key + " :"
    #value = ";" + value + " :"
    dict[key] = value
# 2、读取数据
content = {}
for line in f:
    str = line
    for key in dict:
        regex = "[;{]" + key + " :"
        print("%s============"%key)
        #str = str.replace(key , dict[key])
            #.replace(";" , "\n")
        str,num = re.subn(regex, dict[key], str)
    print(str.strip())
    data.write(str)
# 关闭文件
f.close()
dic.close()
data.close()