#打开IMIX数据文件
imix = open("D:/Personal/Desktop/IMIXSource.txt", "r")
#打开MetaObject数据文件
meta = open("D:/Personal/Desktop/Source.txt", "r")
#MetaObject映射表
meta_dic = open("D:/Personal/Desktop/dic.txt", "r")
#IMIX映射表
imix_dic = open("D:/Personal/Desktop/IMIXdic.txt", "r")
data = open("D:/Personal/Desktop/data.txt", "w")

#读取IMIX映射表
IMIXdict = {}
for line in imix_dic:
    imix_key,imix_value = line.strip().split(":")
    IMIXdict[imix_key] = imix_value
#读取MetaObject映射表
metaDic = {}
for line in meta_dic:
    meta_key,meta_value = line.strip().split(":")
    metaDic[meta_key] = meta_value

#读取IMIX数据
content = {}
for line in imix:
    try:
        imix_key_old,imix_value_old = line.strip().split(":")
        imix_key = IMIXdict[imix_key_old]
        content[imix_key] = imix_value_old
    except KeyError as keyerr:
        print("key%s:value%s不存在"%(key_old,value_old))
#读取Meta数据
meta_content = {}
for line in meta:
    try:
        meta_key_old,meta_value_old = line.strip().split(":")
        meta_key = metaDic[meta_key_old]
        meta_content[meta_key] = meta_value_old
    except KeyError as keyerr:
        print("读取Meta数据：key%s:value%s在MetaObject中不存在"%(meta_key,meta_value_old))
#比对数据
for key in content:
    try:
        if content[key] == meta_content[key]:
            print("数值一致：%s在IMIX中的值为%s，在MetaObject中的值为%s"%(key,content[key],meta_content[key]))
        else:
            print("数值不一致：%s在IMIX中的值为%s，在MetaObject中的值为%s" % (key, content[key], meta_content[key]))
    except KeyError as keyerr:
        print("比对数据：key%s在MetaObject中不存在不存在:IMIX_value%s" % (key, content[key]))
# 关闭文件
imix.close()
meta.close()
meta_dic.close()
imix_dic.close()
data.close()