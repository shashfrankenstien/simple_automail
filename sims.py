import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


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
			self.server.sendmail(msg.sender, msg.recipient, str(msg.message))
			self.server.close()
		except Exception, e: 
			print '\n\n',str(e), '\n\n'
		Mail._count += 1

	