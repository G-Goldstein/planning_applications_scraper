import datetime

def format_for_site(date=None):
  if not date:
  	date = datetime.datetime.now()
  return date.strftime('%d %b %Y')

def format_from_site(datestring):
	return datetime.datetime.strptime(datestring, '%a %d %b %Y').date()