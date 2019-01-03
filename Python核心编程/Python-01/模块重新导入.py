import sys
print("增加前:"+str(sys.path))
sys.path.append("F:\云盘同步文件夹\我的坚果云\PycharmProject\Python核心编程\Python-01")
print("增加后:"+str(sys.path))
'''
"H:\Program Files\Python\Python37\python.exe" F:/云盘同步文件夹/我的坚果云/PycharmProject/Python核心编程/Python-01/模块重新导入.py
增加前:['F:\\云盘同步文件夹\\我的坚果云\\PycharmProject\\Python核心编程\\Python-01', 'F:\\云盘同步文件夹\\我的坚果云\\PycharmProject', 'H:\\Program Files\\Python\\Python37\\python37.zip', 'H:\\Program Files\\Python\\Python37\\DLLs', 'H:\\Program Files\\Python\\Python37\\lib', 'H:\\Program Files\\Python\\Python37', 'H:\\Program Files\\Python\\Python37\\lib\\site-packages', 'H:\\Program Files\\Python\\Python37\\lib\\site-packages\\wheel-0.29.0-py3.7.egg']
增加后:['F:\\云盘同步文件夹\\我的坚果云\\PycharmProject\\Python核心编程\\Python-01', 'F:\\云盘同步文件夹\\我的坚果云\\PycharmProject', 'H:\\Program Files\\Python\\Python37\\python37.zip', 'H:\\Program Files\\Python\\Python37\\DLLs', 'H:\\Program Files\\Python\\Python37\\lib', 'H:\\Program Files\\Python\\Python37', 'H:\\Program Files\\Python\\Python37\\lib\\site-packages', 'H:\\Program Files\\Python\\Python37\\lib\\site-packages\\wheel-0.29.0-py3.7.egg', 'F:\\云盘同步文件夹\\我的坚果云\\PycharmProject\\Python核心编程\\Python-01']
'''

