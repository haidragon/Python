# 1、打开文件
f = open("D:/Personal/Desktop/Source.txt", "r")

#读取映射表
dic = open("D:/Personal/Desktop/dic.txt", "r")
data = open("D:/Personal/Desktop/data.txt", "w")
dict = {}
for line in dic:
    key,value = line.strip().split(":")
    dict[key] = value


# 2、读取数据
content = {}
for line in f:
    try:
        #print(line.strip())
        key_old,value_old = line.strip().split(":")
        #print("key_old=%s"%key_old)
        key = dict[key_old]
        #print("="*20)
        #print(key)
        #print(value)
        #print("=" * 20)
        #content[key] = value
        str = key + "(" + key_old + ")" + ":" + value_old + "\n"
        print(str.strip())
        data.write(str)
    except KeyError as keyerr:
        print("key:%s不存在\tvalue:%s" % (key_old, value_old))
        str1 = key_old + ":" + value_old + "\n"
        data.write(str1)
# 关闭文件
f.close()
dic.close()
data.close()
