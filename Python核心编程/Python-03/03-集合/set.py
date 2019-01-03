a = "abcdef"
b = set(a)#{'c', 'b', 'a', 'e', 'd', 'f'}
#print(b)
A = "bdfhuy"
B = set(A)
#print(B)#{'d', 'f', 'b'}

print(b&B)#交集：同时存在b和B{'b', 'd', 'f'}
print(b|B)#并集：两个集合合并去重后{'b', 'f', 'a', 'u', 'y', 'e', 'c', 'd', 'h'}
print(b-B)#差集：在b不在B的{'e', 'c', 'a'}
print(b^B)#对称差集，不在b也不在B的-并集减去交集{'e', 'u', 'a', 'y', 'h', 'c'}










