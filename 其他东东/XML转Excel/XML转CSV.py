#coding:utf-8
#import sys
#sys.setdefaultencoding('utf-8')
#上面4行处理utf-8字符编码

#引入PythonET包
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tableCount = 0

def getUmlClass(node, path):
    global tableCount   #使用全局变量
    target_tag = "UML.Class"
    path = path + '->' + node.tag   #取XML节点的tag
    if node.tag == target_tag:
        tableCount = tableCount + 1
        getUmlAttribute(node)
        print >> csvFile, ''    #将空行写入文件
    else:
        for child in node:  #子节点遍历
            getUmlClass(child, path)    #递归调用

def getUmlAttribute(nodeClass):
    tableName = nodeClass.attrib['name']    #取XML节点属性
    print >> csvFile,'TAB_INFO,'+tableName  ##将表名写入文件
    #nodeFeature = nodeClass.find('UML.Classifier.feature')  #查找tag为UML.Classifier.feature的子节点
    nodeFeature = nodeClass.find('IMIXML.Remider')  #查找子节点
    print(nodeFeature)
    if nodeFeature == None:
        return
    for nodeAttribute in nodeFeature.findall("UML.Attribute"):  #遍历所有tag为UML.Attribute的子节点
        columnName = nodeAttribute.attrib['name']
        columnType = 'Integer'
        columnLength = '0'
        columnPrecision = '0'
        columnScale = '0'
        columnDesc = 'empty'
        nodeColumnInfo = nodeAttribute.find('UML.ModelElement.taggedValue')
        for info in nodeColumnInfo.findall('UML.TaggedValue'):
            if info.attrib['tag'] == 'type':
                columnType = info.attrib['value']
            elif info.attrib['tag'] == 'length':
                columnLength = info.attrib['value']
            elif info.attrib['tag'] == 'precision':
                columnPrecision = info.attrib['value']
            elif info.attrib['tag'] == 'scale':
                columnScale = info.attrib['value']
            elif info.attrib['tag'] == 'description':
                columnDesc = info.attrib['value']
        print >> csvFile, 'COL_INFO,'+columnName+','+columnType ##将列信息写入文件

csvFile = open("C:/Users/xiaoming/Desktop/output.csv", "w")   #打开文件写入
tableCount = 0
#try:
#    tree = ET.parse("input.xml")     #打开xml文档
#    root = tree.getroot()         #获得root节点
#except (Exception e):
#    print("Error:cannot parse file:input.xml.")
#    sys.exit(1)

tree = ET.parse("C:/Users/xiaoming/Desktop/下30个自然日交易提示_20190410.xml")     #打开xml文档
root = tree.getroot()         #获得root节点
getUmlClass(root, "")
csvFile.close()
print("create",tableCount," tables from input.xml")
