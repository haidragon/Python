# 1、打开文件
f = open("D:/Personal/Desktop/IMIXSource.txt", "r")

#读取映射表
dic = open("D:/Personal/Desktop/IMIXdic.txt", "r")
data = open("D:/Personal/Desktop/IMIXdata.txt", "w")
IMIXdict = {}
for line in dic:
    key,value = line.strip().split(":")
    IMIXdict[key] = value
# 2、读取数据
content = {}
for line in f:
    try:
        #print(line.strip())
        key_old,value_old = line.strip().split(":")
        #print("key_old=%s"%key_old)
        key = IMIXdict[key_old]
        value = value_old
        #print("="*20)
        #print(key)
        #print(value)
        #print("=" * 20)
        #content[key] = value
        str = key + ":" + value_old + "\n"
        data.write(str)
    except KeyError as keyerr:
        print("key%s:value%s不存在"%(key_old,value_old))
# 关闭文件
f.close()
dic.close()
data.close()