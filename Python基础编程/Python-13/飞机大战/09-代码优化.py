a = [11,22,33,44,55]
for i in a:
    if i == 33 or i == 44:
        a.remove(i)
print(a)
#[11, 22, 44, 55] 会漏删,列表在循环过程中删除自身元素会导致漏删


b = [11,22,33,44,55]
c = []
for i in b :
    if i == 33 or i == 44:
        c.append(i)
#列表在循环过程中删除自身元素会导致漏删，但在自身循环过程中可以删除其他列表元素
for i in c:
    b.remove(i)
print(b)
#[11, 22, 55]