def test(num):
    if num > 1:
        return num*test(num-1)
    else:
        return num

result = test(4)
print(result)

def test2(num):
    if num >= 0 :
        print(num)
        test2(num-1)
    else:
        return
test2(5)
