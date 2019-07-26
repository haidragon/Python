info = {"name": "laowang", "age": 18}
# 遍历key
for temp in info.keys():
    print(temp)
# 遍历value
for temp in info.values():
    print(temp)
# 遍历items
#Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。
info_Item = info.items()
print(info_Item)
#打印字典内的数据
#方法一：直接打印元组
for temp in info.items():
    print(temp)

'''结果：
('name', 'laowang')
('age', 18)'''


print("="*50)
#方法二:下标
for temp in info.items():
    print("key=%s,value=%s"%(temp[0],temp[1]))

'''结果：
    key = name, value = laowang
    key = age, value = 18'''

print("="*50)
#方法三:拆包
for temp1,temp2 in info.items():
    print("key=%s,value=%s"%(temp1,temp2))

'''结果：
    key = name, value = laowang
    key = age, value = 18'''