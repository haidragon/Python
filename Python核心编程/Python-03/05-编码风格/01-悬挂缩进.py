#第一行有参数->对齐左括号
foo = long_function(one,two,
                    three,four)

#第一行无参数->不对准左括号，但增加一层缩进
def long_function1(
        one,two,
        three,four):
    print(one)

#if多个条件增加括号，并在第一行和第二行之间增加缩进
if  (this_is_one_thing
        and this_is_another_thing):
    do_something()


#内容缩进，括号对齐变量名
list1 = [
    1,2,3,4,
    5,6,7,8,
]