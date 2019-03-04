def open_file():
    try:
        file = open(input("请输入文件路径，类似E:\云盘同步文件夹\str2.jpg\n"), "rb")
        print("openfile中的file=%s"%str(file))
        return file
    except IOError as e:
        print("请输入正确的文件路径")
        return open_file()


f = open_file()
print("openfile中的file=%s"%str(f))


