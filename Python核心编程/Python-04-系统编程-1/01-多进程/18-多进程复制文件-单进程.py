import os
import time
#print(os.listdir())

def u_listFile(dirPath,fileList):
    #print("1=====%s"%dirPath)
    if not os.path.isdir(dirPath):
        #print("文件1========%s========" % os.path.realpath(dirPath))
        fileList.append(dirPath)
    else:
        #print("文件夹1========%s========" % os.path.realpath(dirPath))
        dirPath = os.path.join(dirPath,dirPath)
        for i in os.listdir(dirPath):
            #print("2=====%s"%os.path.realpath(dirPath))
            #print("3=====%s"%os.path.realpath(i))
            #u_listFile(os.path.realpath(i),fileList)
            u_listFile(os.path.join(dirPath,i), fileList)
    return fileList

def copy_file(path):

    fileListFrom = []
    fileListTo = []
    f = u_listFile(path,fileListFrom)
    for pathFrom in f:
        pathTo = pathFrom.replace("G:\\Testing", "G:\\Testing-copy")
        #fileListTo.append(pathTo)
        # 创建拷贝文件夹(多层文件夹使用os.makedirs(path)创建)
        pathToDir = os.path.dirname(pathTo)
        print(pathToDir)
        print("="*20)
        if os.path.exists(pathToDir):
            print("%s is exist"%pathToDir)
        else:
            os.makedirs(pathToDir)

        fileTo = open(pathTo, "wb")
        print("读取成功")
        fileFrom = open(pathFrom, "rb")
        print("准备写入")
        for line in fileFrom:
            fileTo.write(line)
        fileTo.close()
        fileFrom.close()
    #return fileListTo


if __name__ == "__main__":
    timeStart = time.time()
    #path = r'C:\Users\xiaoming\Desktop\test'
    path = r"G:\Testing"

    copy_file(path)
    timeEnd = time.time()
    print("耗时%s"%(timeEnd - timeStart))

