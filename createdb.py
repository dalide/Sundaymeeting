import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE users (name TEXT, city TEXT, addr TEXT, zipcode TEXT)')
print("Table created successfully")
conn.close()