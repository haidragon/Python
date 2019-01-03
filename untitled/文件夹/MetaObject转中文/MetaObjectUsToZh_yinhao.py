#coding=utf-8
# 1、打开文件
f = open("./Source.txt", "r")
#读取映射表
dic = open("./dic.txt", "r")
data = open("./data.txt", "w")
str = ""
dict = {}
dict_1 = {}
for line in dic:
    key,value = line.strip().split(":")
    key = "\"" + key + "\""
    value = "\"" + value + "\""
    dict[key] = value
# 2、读取数据
for line in f:
    str = line
    for key in dict:
        print("%s============"%key)
        str = str.replace(key , dict[key])
            #.replace(";" , "\n")
    #print(str.strip())
    data.write(str)
# 关闭文件
f.close()
dic.close()
data.close()