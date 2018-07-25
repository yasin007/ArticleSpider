"""
create by 维尼的小熊 on 2018/7/25

"""
__autor__ = 'yasin'

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

# 设置服务器(我用的gmail，你们用的什么就换成什么
# 比如qq，163～记得登录网页版邮箱然后在设置里面修改支持smtp
mail_host = "smtp.exmail.qq.com"
# 用户名
mail_user = "yangyi@gogpay.cn"
# 邮箱密码
mail_pass = "yy6831062"

sender = 'yangyi@gogpay.cn'
receivers = ['18922619@qq.com', 'ranchengcheng@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 读取我的自动爬虫获取的内容
F = open("/Users/yiyang/Desktop/ArticleSpider/ArticleSpider/tools/32111.html")
# list改成str格式，否则编码不通过
f = F.read()

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText(f, 'html', 'utf-8')
message['From'] = Header("your remote server", 'utf-8')
message['To'] = Header("my lorder", 'utf-8')
t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
subject = '多彩宝公司热搜前50-邮件分析发布\n' + t
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.set_debuglevel(1)
    # smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
