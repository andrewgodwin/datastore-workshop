import psycopg2

# Get the IP address of the docker container "postgresql"
import json, subprocess
host = json.loads(subprocess.check_output(["docker", "inspect", "postgresql"]))[0]["NetworkSettings"]["IPAddress"]

# Make the client
conn = psycopg2.connect("dbname=test user=postgres host=%s password=password" % host)
cursor = conn.cursor()

cursor.execute("CREATE TABLE testing (id serial PRIMARY KEY, name VARCHAR, age INT)")
cursor.execute("INSERT INTO testing (name, age) VALUES ('Amy', 27), ('Bob', 32)")

cursor.execute("SELECT * FROM testing")
print cursor.fetchall()

cursor.execute("SELECT name, age + 10 FROM testing")
print cursor.fetchall()
