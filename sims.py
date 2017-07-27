import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.application import MIMEApplication 


class Message(object):
	'''Takes recipient, sender, subject and body to initiate'''
	def __init__(self, recipient='', sender='', subject='', body=''):
		print recipient, sender, subject, body
		self.message = MIMEMultipart()
		self.sender = sender
		self.recipient = recipient
		self.setHeader(recipient, sender, subject)
		self.setBody(body)

	def setHeader(self, recipient, sender, subject):
		self.message['From'] = sender
		self.message['To'] = recipient
		self.message['Subject'] = subject

	def setBody(self, body):
		self.message.attach(MIMEText(body, 'plain'))

	def attachment(self, binary, filename):
		part = MIMEApplication(binary, Name=filename)
		part['Content-Disposition'] = 'attachment; filename="%s"' % filename
		self.message.attach(part)



class Mail(object):
	"""
	It takes MAIL_USERNAME, MAIL_PASSWORD and MAIL_SERVER_PORT to initiate.
	the 'send' method takes a Message object as an argument.
	"""
	_count = 0

	def __init__(self, username, password, mail_server_port):
		self.username = username
		self.password = password
		self.host_port = mail_server_port
		self.server = smtplib.SMTP()
		self.server.set_debuglevel(1)

	def send(self, msg):
		try:
			self.server.connect(self.host_port)
			self.server.ehlo()
			self.server.starttls()
			self.server.login(self.username,self.password)
			print('logged in ')
			self.server.sendmail(msg.sender, msg.recipient, str(msg.message))
			print('sent')
			self.server.close()
			print('closed')
		except Exception, e: 
			print '\n\n',str(e), '\n\n'
		Mail._count += 1

if __name__ == '__main__':
	m = Message('shashank.gopikrishna@gmail.com', 'shashank.parodize@gmail.com', subject='Attachment Test', body='yolo')
	with open('./sims.py', 'rb') as f:
		m.attachment(f.read(), 'sims.py')
	Mail('shashank.parodize@gmail.com', 'TakeMeDownToParodizeCity', 'smtp.gmail.com:587').send(m)