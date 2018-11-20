import scraper, datetime, post_application

sesh = scraper.Site_Session()

#for historic_weeks_beginning = 

for days_ago in range(1, 365*5, 7): # Once a week for the past 5 years
	applications = sesh.applications_for_week_commencing(datetime.datetime.now() - datetime.timedelta(days=days_ago))

	for application in applications:
		print(application)
		post_application.post_application(application)

