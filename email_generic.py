# Following code will send email to abc@gmail.com from xyz@gmail.com and 
# the message content will be from index.html

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Another planet'
# abc@gmail.com is receiver's email id
email['to'] = 'abc@gmail.com'
email['subject'] = 'Hello world'
email.set_content(html.substitute({'name':'Bob','age': '20'}),'html')

# following only works for gmail id
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	# xyz@gmail.com is sender's email address and 
	# pass123 is sender's email id password
	smtp.login('xyz@gmail.com','pass123')
	print('all good boss!!')