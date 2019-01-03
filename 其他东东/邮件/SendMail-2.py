# coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr
from email.header import Header

# 设置smtplib所需的参数
# 下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.exmail.qq.com'
username = 'wanghongming@ectesting.cn'
password = 'Ming@123'
sender = 'wanghongming@ectesting.cn'
# receiver='XXX@126.com'
# 收件人为多个收件人
receiver = ['540168246@qq.com', 'wang1284919002@163.com']

def mail():
    ret = True
    try:
        subject = 'Python email test'
        # 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
        # subject = '中文标题'
        # subject=Header(subject, 'utf-8').encode()
        # 构造邮件对象MIMEMultipart对象
        # 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
        msg = MIMEMultipart('mixed')
        #邮件主题
        msg['Subject'] = subject
        #导入from email.utils import formataddr，可通过formataddr设置别名
        #发件人
        msg['From'] = formataddr(["ming", sender])
        # msg['To'] = 'XXX@126.com'#单个收件人
        # 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
        msg['To'] = ";".join(receiver)
        # msg['Date']='2012-3-16'

        # 构造文字内容（此内容会被下面的html内容覆盖掉）
        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"
        text_plain = MIMEText(text, 'plain', 'utf-8')
        msg.attach(text_plain)

        # 构造图片链接（图片附件）
        sendimagefile = open(r'E:\软件\360图片\0.png', 'rb').read()
        image = MIMEImage(sendimagefile)
        image.add_header('Content-ID', '<image1>')
        #将图片作为附件
        image["Content-Disposition"] = 'attachment; filename="test0.png"'
        msg.attach(image)

        # 构造html
        # 发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
        html = """
        <html>  
          <head></head>  
          <body>  
            <p>Hi!<br>  
               雷猴<br>  
               Here is the <a href="http://www.baidu.com">链接</a> you wanted.<br> 
            </p> 
          </body>  
        </html>  
        """
        text_html = MIMEText(html, 'html', 'utf-8')
        #将html当做附件发出
        #text_html["Content-Disposition"] = 'attachment; filename="testhtml.html"'
        msg.attach(text_html)

        # 构造附件
        sendfile = open(r'E:\软件\uebaodian.rar', 'rb').read()
        text_att = MIMEText(sendfile, 'base64', 'utf-8')
        text_att["Content-Type"] = 'application/octet-stream'
        # 以下附件可以重命名成aaa.txt
        # text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
        # 另一种重命名方式
        text_att.add_header('Content-Disposition', 'attachment', filename='uebaodian.rar')
        # 以下中文测试不ok
        # text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
        msg.attach(text_att)

        # 发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
        smtp.set_debuglevel(1)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
