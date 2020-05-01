from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
import smtplib

from_addr = input("enter send address:")
to_addr = input("enter receive address:")
from_token = input("enter password:")
smtp_addr = input("enter smtp address:")
subject = input("enter some subject:")
content = input("now, show ur content:")

# if u want to have a multipart content of ur email, please use 'alternative'
msg = MIMEMultipart('alternative')
# capitalizes the first letter
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header(subject)
# add attach 
msg.attach = MIMEText(content, 'plain', 'utf-8')
# or usr html type
# first param is ur html codes
msg.attach = MIMEText('', 'html', 'utf-8')

with open('#图片地址', 'rb') as fp:
	# if docx, first param is application
	mime = MIMEBase('image','png',filename='test.png')
	mime.add_header('Content-Disposition', 'attachment', filename='1.png')
	# use content-id at html-type content for img src
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')

	# read attach 
	mime.set_payload(f.read())
	# use base64
	encoders.encode_base64(mime)
	# add attach 
	msg.attach(mime)

# smtp default port = 25
server = smtplib(smtp_addr, 25)
# debug able
server.set_debuglevel(1)
# login from email
server.login(from_addr, from_token)
# send mail
server.sendmail(from_addr, [to_addr], msg.as_string())
# stop server
server.quit()

# about mimetype https://www.w3school.com.cn/media/media_mimeref.asp
