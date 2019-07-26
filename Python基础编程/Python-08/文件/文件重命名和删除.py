import os

#获取当前目录:没有文件会报异常
pwd = os.getcwd()
print(pwd)

#改变默认目录:没有文件会报异常
os.chdir("D:/Personal/Desktop")
pwd = os.getcwd()
print(pwd)

#获取目录列表:没有文件会报异常
listDir = os.listdir("D:/Personal/Desktop1")
print(listDir)

#删除文件夹:没有文件会报异常
os.rmdir("D:/Personal/Desktop/test")

#os.remove("D:/Personal/Desktop/test2.txt")
#os.rename("D:/Personal/Desktop/test.txt","D:/Personal/Desktop/test2.txt")
#os.mkdir("D:/Personal/Desktop/test")