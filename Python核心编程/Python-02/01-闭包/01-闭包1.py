def test(number):
    print("--1--")
    def test_in(number2):
        print("--2--")
        print(number+number2)

    print("--3--")
    return test_in

ret = test(100)
print("-"*30)
#ret()
ret(1)
ret(100)
'''
--1--
--3--
------------------------------
--2--
101
--2--
200
'''