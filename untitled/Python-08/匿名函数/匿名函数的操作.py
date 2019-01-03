#列表排序
arr = [11,22,1,3,4,1,55,89]
arr.sort()
print(arr)

#字典排序
info = [{"age": 18, "name": "laowang"}, {"age": 15 ,"name":"xiaoming"}, {"age": 21,"name":"laoli"}]
info.sort(key=lambda x:x['age'])
print(info)
