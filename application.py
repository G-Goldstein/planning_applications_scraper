import os

URL_PREFIX = os.environ['URL_PREFIX']

class Application():
	def __init__(self, title, url, address, reference, received_date, validated_date, status):
		self.title = title
		self.url = URL_PREFIX + url
		self.address = address
		self.reference = reference
		self.received_date = received_date
		self.validated_date = validated_date
		self.status = status

	def __str__(self):
		return self.title + '\n' + self.address + '\n' + \
		'Ref. No: ' + self.reference + ' | ' + \
		'Received: ' + str(self.received_date) + ' | ' + \
		'Validated: ' + str(self.validated_date) + ' | ' + \
		'Status: ' + self.status + '\n' + \
		self.url