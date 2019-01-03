#coding=utf-8

def openfile():
    global f
    global dic
    global data
    global str
    global dict
    global dict_1
    # 1、打开文件
    f = open("./Source.txt", "r")
    # 读取映射表
    dic = open("./dic.txt", "r")
    data = open("./data.txt", "w")

def wtiteAndCloseFile(str_temp):
    data.write(str_temp)
    # 关闭文件
    f.close()
    dic.close()
    data.close()

def  replaceMetaObj():
    openfile()
    dict = {}
    dict_1 = {}
    for line in dic:
        key, value = line.strip().split(":")
        key = "\"" + key + "\""
        value = "\"" + value + "\""
        dict[key] = value
    # 2、读取数据
    for line in f:
        str = line
        for key in dict:
            print("%s============" % key)
            str = str.replace(key, dict[key])
    wtiteAndCloseFile(str)

def replaceMetaObjSpace():
    openfile()
    dict = {}
    dict_1 = {}
    for line in dic:
        key, value = line.strip().split(":")
        key_1 = "{" + key + " :"
        key = ";" + key + " :"
        value_1 = "{" + value + " :"
        value = ";" + value + " :"
        dict[key] = value
        dict_1[key_1] = value_1
    # 2、读取数据
    for line in f:
        str = line
        for key in dict:
            str = str.replace(key, dict[key])
        for key_1 in dict_1:
            print("%s============" % key_1)
            str = str.replace(key_1, dict_1[key_1])
    wtiteAndCloseFile(str)
def replaceMetaObjNoSpace():
    openfile()
    dict = {}
    dict_1 = {}
    for line in dic:
        key, value = line.strip().split(":")
        key_1 = "{" + key + ":"
        key = ";" + key + ":"
        value_1 = "{" + value + ":"
        value = ";" + value + ":"
        dict[key] = value
        dict_1[key_1] = value_1
    # 2、读取数据
    for line in f:
        str = line
        for key in dict:
            str = str.replace(key, dict[key])
        for key_1 in dict_1:
            print("%s============" % key_1)
            str = str.replace(key_1, dict_1[key_1])
    wtiteAndCloseFile(str)

def main():
    replaceMetaObj()
    replaceMetaObjSpace()
    replaceMetaObjNoSpace()

if __name__ == "__main__":
    main()

