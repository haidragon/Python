import os
import time
from multiprocessing import Pool,Manager

#创建遍历文件方法
def u_listFile(dirPath,fileList):
    #当文件非文件夹时，添加到列表中
    if not os.path.isdir(dirPath):
        fileList.append(dirPath)
    else:
        #当为文件夹时，使用递归直至为文件
        for i in os.listdir(dirPath):
            #递归
            # 拼接文件路径os.path.join，否则会在工作目录下寻找文件，导致问题出现
            u_listFile(os.path.join(dirPath,i), fileList)
    return fileList

def copy_file(pathFrom, queue):
    #创建一个拷贝路径
    pathTo = pathFrom.replace("G:\\Testing", "G:\\Testing-copy")
    #os.path.dirname，获取文件的路径，若是basename则是获取文件名
    pathToDir = os.path.dirname(pathTo)
    if not os.path.exists(pathToDir):
        # 创建拷贝文件夹(多层文件夹使用os.makedirs(path)创建)
        os.makedirs(pathToDir)
    else:
        pass
    fileTo = open(pathTo, "wb")
    fileFrom = open(pathFrom, "rb")
    for line in fileFrom:
        fileTo.write(line)
    fileTo.close()
    fileFrom.close()
    queue.put(pathTo)

def main(path):
    #创建一个进程池
    po = Pool(4)
    # 创建一个queue用于通信
    queue = Manager().Queue(5000)
    fileListFrom = []
    #获取文件列表
    f = u_listFile(path, fileListFrom)
    for pathFrom in f:
        #启动进程
        po.apply_async(copy_file, args=(pathFrom, queue))

    allNum = len(f)
    num = 0
    print("allNum=%d"%allNum)
    #while True:
    while num < allNum:
        queue.get()
        num += 1
        copy_Rate = num/allNum
        print("进度num=%d：%.2f%%"%(num,copy_Rate*100))
        #if num == allNum:
        #   break

if __name__ == "__main__":
    timeStart = time.time()
    #path = r'C:\Users\xiaoming\Desktop\test'
    path = r"G:\Testing"
    main(path)
    timeEnd = time.time()
    print("耗时%s"%(timeEnd - timeStart))

