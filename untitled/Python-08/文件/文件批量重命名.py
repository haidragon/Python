import os
#创建文件夹
#os.mkdir("D:/Personal/Desktop/test/")
#打开源文件
oldFile = open("D:/Personal/Desktop/test.txt")
#oldFileString = oldFile.readlines()
i = 1
#如果源文件存在
if oldFile:
    while i < 10 :
        #拼接新文件名
        newName = "D:/Personal/Desktop/test/test-" + str(i) + ".txt"
        #打开新文件
        newFile = open(newName,'w')
        #循环将源文件内容写入新文件
        for temp in oldFile.readlines():
            newFile.write(temp)
        #关闭新文件
        newFile.close()
        i += 1
        #将源文件的读写位置重定向到文件开头0字节
        oldFile.seek(0,0)
#关闭源文件
oldFile.close()