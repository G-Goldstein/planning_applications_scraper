from bs4 import BeautifulSoup
from application import Application
import re
import dateformatter as df

def applications_from_page(page):
	soup = BeautifulSoup(page, 'html.parser')
	for result in soup.find_all(class_='searchresult'):
		yield html_to_application(result)

def html_to_application(html):
	heading = html.find('a')
	metainfo = html.find('p', class_='metaInfo').get_text()
	ref = re.search(r'Ref\.\sNo:\s*([\d\w/]*)', metainfo).group(1)
	received = re.search(r'Received:\s*([\d\w]+(\s[\d\w]+)*)', metainfo).group(1)
	validated = re.search(r'Validated:\s*([\d\w]+(\s[\d\w]+)*)', metainfo).group(1)
	status = re.search(r'Status:\s*(\w+)', metainfo).group(1)
	return Application(heading.string.strip(),
		               heading.get('href'),
		               html.find('p', class_='address').string.strip(),
		               ref,
		               df.format_from_site(received),
		               df.format_from_site(validated),
		               status
		               )