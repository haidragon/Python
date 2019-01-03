def test():
    i = 0
    while i < 5:
        #当把yield赋值给变量时，由于执行顺序为先执行等号右边，所以第一次执行时会卡在yield
        #当第二次执行时会总temp赋值开始，但是此时temp的右边为空
        #所以执行第二个next()或者__next__()时，temp为None
        #当执行send()方法时，send("aaa")中的aaa表示替代了yield i，将aaa赋值给temp，并且生成器向下执行一步
        temp = yield i
        print(temp)
        i += 1
a = test()
a.__next__()
a.__next__()#None
a.send("aaa")#aaa
a.__next__()#None
