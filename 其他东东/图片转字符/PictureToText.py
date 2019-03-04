from PIL import Image

def get_Text(img):
    img = img.convert("L")
    charlist = ""
    for h in range(0, img.size[1]):
        for w in range(0, img.size[0]):
            gray = img.getpixel((w, h))
            pos = gray / 256
            charlist = charlist + codelist[int((count -1) * pos)]
        charlist = charlist + "\r"
    return charlist

def open_file():
    try:
        file = open(input("请输入文件路径，类似E:\云盘同步文件夹\str2.jpg\n"), "rb")
        return file
    except IOError as e:
        print("请输入正确的文件路径")
        #调用函数的时候，如果没有执行 return 命令（或 return 命令未接收数据），默认会返回 none
        #所以如果这里不加return的话，那么就相当于openfile这个函数没执行到return
        #则接受它返回值的变量就会获得一个none，所以在这里加一个none，获得openfile的返回值再返回才可以，不然的话
        #再次调用openfile()，只不过是在openfile()内部获得了一个返回值，并没有返回到真正接受
        #这个返回值的变量
        return open_file()

def getImage():
    file = open_file()
    img = Image.open(file)
    print("返回完成")
    return img

def trantxt():
    outfile = open("tmp.txt", "w")
    outfile.write(get_Text(img))
    outfile.close()

if __name__ == '__main__':
    img = getImage()
    print(img)
    width, heigth = img.size[0], img.size[1]

    codelist = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/" \
               "\|()1{}[]?-_+~<>i!lI;:,\"^`."

    count = len(codelist)
    scale = width / heigth
    img = img.resize((int(width * 0.2), int(width * 0.1 /scale)))
    trantxt()
