import scraper, datetime, post_application

sesh = scraper.Site_Session()

#for historic_weeks_beginning = 

while True:
	for days_ago in range(1, 30, 7): # Once a week for the past month
		applications = sesh.applications_for_week_commencing(datetime.datetime.now() - datetime.timedelta(days=days_ago))

		for application in applications:
			print(application)
			post_application.post_application(application)
	sleep(60*60*23) # Sleep for almost a day, to make sure we do run every day.

