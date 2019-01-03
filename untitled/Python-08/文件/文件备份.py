#打开即将备份的文件
oldFileName = "D:/Personal/Desktop/test.txt"
oldFile = open(oldFileName,"r")

#如果打开了文件，则继续进行操作
if oldFile:
    #获取文件后缀名
    '''
    rfind(".") :返回子字符串(".")最后一次出现在字符串中的索引位置
    如果子字符串不在字符串中返回-1
    '''
    fileFlagNum = oldFileName.rfind(".")
    #如果文件名中有“.”则继续操作
    if fileFlagNum > 0:
        fileFlag = oldFileName[fileFlagNum:]
    #组织新的文件名：
    newFileName = oldFileName[:fileFlagNum] + "[副本]" + fileFlag
    #创建新的文件
    newFile = open(newFileName,'w')
    #将原文件中的数据复制到新文件中
    for temp in oldFile.readlines():
        newFile.write(temp)
#关闭文件
oldFile.close()
newFile.close()