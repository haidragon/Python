from urllib import request
image_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1565023435453&di=a027ae39e9d3974ebdb5d1090c353f38&imgtype=0&src=http%3A%2F%2Fgss0.baidu.com%2F9fo3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2F72f082025aafa40f698d35b7aa64034f78f01914.jpg"
respone = request.urlopen(image_url)
#f = open("image.gif","wb")
#f.write(respone.read())

with open("image2.jpg","wb") as fb:
    fb.write(respone.read())
