#定义一个函数，参数为a,b,c
def test(a,b,c):
    result = c(a,b)
    print(result)

func_new = input("请输入一个匿名函数")
func_new = eval(func_new)
#调用函数，输入参数a=11,b=22,c=一个匿名函数
#Python函数的实参可以是函数和匿名函数
test(11,22,func_new)