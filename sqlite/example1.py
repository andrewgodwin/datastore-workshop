import sqlite3

# Make the client
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE testing (id serial PRIMARY KEY, name VARCHAR, age INT)")
cursor.execute("INSERT INTO testing (name, age) VALUES ('Amy', 27), ('Bob', 32)")

cursor.execute("SELECT * FROM testing")
print cursor.fetchall()

cursor.execute("SELECT name, age + 10 FROM testing")
print cursor.fetchall()
