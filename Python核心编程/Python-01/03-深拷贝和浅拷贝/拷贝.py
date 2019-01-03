import copy
a = [11,22,33]
b = a
print(id(a))#2064261931592
print(id(b))#2064261931592

print("="*20)
c = copy.deepcopy(a)
print("a=%s"%str(a))
print("c=%s"%str(c))
print("id(a)=%s"%id(a))
print("id(c)=%s"%id(c))
'''
a=[11, 22, 33]
c=[11, 22, 33]
id(a)=1659761108040
id(c)=1659761252488
'''

