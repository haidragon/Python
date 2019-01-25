import os
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

if __name__ == "__main__":
    path = r'C:\Users\xiaoming\Desktop\test'
    os.chdir(path)
    #print("=====%s"%os.listdir(path))
    fileList = []
    f = u_listFile(path,fileList)
    print(f)

