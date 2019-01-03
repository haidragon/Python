import functools
temp1 = functools.reduce(lambda x,y:x+y,[1,2,3,4,5],-20)
print(temp1)
#-5

temp2 = functools.reduce(lambda x,y:x+y,["aa","bb","cc"],"dd")
print(temp2)
#ddaabbcc
