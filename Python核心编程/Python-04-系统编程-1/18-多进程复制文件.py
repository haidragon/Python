import os
#print(os.listdir())
def u_listDir(dirList,fileList):
    for dirPath in dirList:
        #print(dirPath)
        if not os.path.isdir(dirPath):
            print("文件1========%s========" % os.path.realpath(dirPath))
            fileList.append(dirPath)
        else:
            print("文件夹1========%s========" % os.path.realpath(dirPath))
            u_listFile(dirPath,fileList)
    return fileList


def u_listFile(dirPath,fileList):
    for i in os.listdir(dirPath):

        if not os.path.isdir(i):
            print("文件========%s========" % os.path.realpath(i))
            fileList.append(i)
        else:
            print("文件夹========%s========" % os.path.realpath(i))
            u_listDir(i,fileList)
    return fileList

if __name__ == "__main__":
    os.chdir(r'C:\Users\xiaoming\Desktop\test')
    dirList = os.listdir()
    fileList = []
    f = u_listDir(dirList,fileList)
    print(f)

