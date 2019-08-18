from androguard import misc
from androguard import session
from androguard import util

# 获取默认session
#sess = misc.get_default_session()

# 保存session到本地-保存失败
session.Save(sess, "H:/其他/srcb/首测/androguard/androguard_session.ag")

# 使用session
#a, d, dx = misc.AnalyzeAPK("C:/Users/ThinkPad/Desktop/com.srcb.qymbank.apk", session=sess)
a, d, dx = misc.AnalyzeAPK("C:/Users/ThinkPad/Desktop/com.srcb.qymbank.apk")
# 显示当前会话信息
#print(sess.show())

# 加载session
#sess = session.Load("H:/其他/srcb/首测/androguard/androguard_session.ag")
#命令行加载session
#androguard analyze --session H:/其他/srcb/首测/androguard/androguard_session.ag


#获取APK的权限
u_permissions = a.get_permissions()
print(u_permissions)
#获取AndroidManifest.xml中定义的所有活动的列表
u_activities = a.get_activities()
print(u_activities)
#获取包名称，应用程序名称和图标路径
u_package = a.get_package()
print(u_package)
u_app_name = a.get_app_name()
print(u_app_name)
u_app_icon = a.get_app_icon()
print(u_app_icon)

#获取数字版本和版本字符串，以及最小，最大，目标和有效的SDK版本
u_androidversion_code = a.get_androidversion_code()
print(u_androidversion_code)
u_androidversion_name = a.get_androidversion_name()
print(u_androidversion_name)
u_get_min_sdk_version = a.get_min_sdk_version()
print(u_get_min_sdk_version)
u_get_max_sdk_version = a.get_max_sdk_version()
print(u_get_max_sdk_version)
u_get_target_sdk_version = a.get_target_sdk_version()
print(u_get_target_sdk_version)
u_effective_target_sdk_version = a.get_effective_target_sdk_version()
print(u_effective_target_sdk_version)

#获取AndroidManifest.xml的解码XML
u_xml = a.get_android_manifest_axml().get_xml()
print(u_xml)

#获取方法调用的XREF（交叉引用）
#返回一个ClassAnalysis对象列表 其中一些标记为EXTERNAL，这意味着此类的源代码未在Analysis内部加载的DEX文件中定义
#从类中查询所有被调用的类
u_classes = dx.get_classes()

#从类中查询所有被调用的类tests.androguard.TestActivity。
# 请记住，您需要提供类名作为带有正斜杠而不是点的类型格式。可以简单地使用classes 或find_classes()获得类
for meth in dx.classes['Lcom/bumptech/glide/load/resource/transcode/GifDrawableBytesTranscoder;'].get_methods():#获取方法
    print("inside method {}".format(meth.name))#打印方法名
    for _, call, _ in meth.get_xref_to():#获取调用
        print("  calling -> {} -- {}".format(call.class_name, call.name))#打印被调用的方法


#外部方法，如API调用，不会为任何XREF提供xref_to()
#使用get_xref_from()
#外部类或方法只是在创建XREF时无法在加载的DEX文件中找到的类或方法！因此，始终加载multidex文件的所有DEX文件非常重要。
# 另一方面，请注意可能未定义类，因为它们可以在以后动态加载。外部并不意味着此类/方法是Android或Java API！
for meth in dx.classes['Ljava/io/File;'].get_methods():#获取类中的方法
    print("usage of method {}".format(meth.name))#打印方法名
    for _, call, _ in meth.get_xref_from():#获取方法的调用（外部方法的话只会被调用）
        print("  called by -> {} -- {}".format( call.class_name, call.name))#打印调用信息

#获取String的XREF（交叉引用）xref_from()
for _, meth in dx.strings['YTTimePicker'].get_xref_from():
    print("Used in: {} -- {}".format(meth.class_name, meth.name))


#获取字段的XREF：xref_read()和xref_write()
#可以使用find_methods来查找字段
#find_methods(classname='.*', methodname='.*', descriptor='.*', accessflags='.*', no_external=False)
for field in dx.find_fields(classname='Ltests/androguard/TestActivity;', fieldname='^value$'):
    print("Field: {}".format(field.name))
    for _, meth in field.get_xref_read():
        print("  read in {} -- {}".format(meth.class_name, meth.name))
    for _, meth in field.get_xref_write():
        print("  write in {} -- {}".format(meth.class_name, meth.name))


#util.get_certificate_name_string(,short = False,delimiter ='，' )





