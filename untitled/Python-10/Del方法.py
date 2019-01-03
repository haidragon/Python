class Dog:
    def __del__(self):
        print("==over==")

dog1 = Dog()
dog2 = dog1

del dog1
print("="*10)

#执行结果
#==========
#==over==