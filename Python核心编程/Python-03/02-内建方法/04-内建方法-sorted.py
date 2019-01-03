a = [5,2,3,4,1]
a.sort()
print(a)
#[1, 2, 3, 4, 5]

b = [5,2,3,4,1]
b.sort(reverse=True)
print(b)
#[5, 4, 3, 2, 1]

print("sorted========>")
print(sorted([1,4,2,3,5]))#由小到大
print(sorted([1,4,2,3,5],reverse=0))#由小到大
print(sorted([1,4,2,3,5],reverse=2))#由大到小
print(sorted(['A','B','D','a','b'],reverse=0))#按照ACSII排序