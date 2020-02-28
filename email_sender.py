import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Another planet'
# abc@gmail.com is receiver's email id
email['to'] = 'abc@gmail.com'
email['subject'] = 'Hello world'
email.set_content('I am Bob.........')

# following only works for gmail id
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	# xyz@gmail.com is sender's email address and 
	# pass123 is sender's email id password
	smtp.login('xyz@gmail.com','pass123')
	smtp.send_message(email)
	print('all good boss!!')