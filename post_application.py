import psycopg2, os

DATABASE_URL = os.environ['DATABASE_URL']

def post_application(application):
	conn = psycopg2.connect(DATABASE_URL)
	cursor = conn.cursor()
	cursor.execute("""
		INSERT INTO application 
		(VALUES (%s, %s, %s, %s, %s, %s, %s))
		ON CONFLICT (reference) DO NOTHING
		""", [application.reference, application.title, application.url, application.address,
		application.received_date, application.validated_date, application.status])
	cursor.execute("COMMIT")