a = [i for i in range(1,18)]
print(a)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

b = [11 for i in range(1,18)]
print(b)
#[11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]

c = [i for i in range(10) if i%2 == 0]
print(c)
#[0, 2, 4, 6, 8]

d = [(i,j) for i in range(3) for j in range(2)]
print(d)
#[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)],双层for循环

#==以下方法等价于以上
d2 = []
for i in range(3):
    for j in range(2):
        d2.append((i,j))
print(d2)
#[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

e = [(i,j,k) for i in range(3) for j in range(2) for k in range(2)]
print(e)
#[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 0, 1), (2, 1, 0), (2, 1, 1)]






