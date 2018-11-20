import requests
import json
import dateformatter as df
import applicationfinder as af
import os

URL_PREFIX = os.environ['URL_PREFIX']

start_url = URL_PREFIX + '/online-applications/search.do'
start_params = {
	'action': 'weeklyList',
}

first_page_url = URL_PREFIX + '/online-applications/weeklyListResults.do'
first_page_params = {
	'action': 'firstPage',
}

paged_url = URL_PREFIX + '/online-applications/pagedSearchResults.do'

def paged_params(page_number):
	return {
		'action': 'page',
		'searchCriteria.page': str(page_number),
	}

class Site_Session():
	def __init__(self):
		self.s = requests.Session()
		r = self.s.get(start_url, params=start_params)

	def _application_pages_for_week_commencing(self, date):
		first_page_form = {
			'searchCriteria.parish': '',
			'searchCriteria.ward': '',
			'week': df.format_for_site(date),
		    'dateType': 'DC_Validated',
    		'searchType': 'Application',
		}

		page_number = 1

		r = self.s.post(first_page_url, params=first_page_params, data=first_page_form)
		while (r.status_code==200):
			yield r.text
			page_number += 1
			r = self.s.post(paged_url, params=paged_params(page_number))

	def applications_for_week_commencing(self, date):
		for page in self._application_pages_for_week_commencing(date):
			yield from af.applications_from_page(page)

