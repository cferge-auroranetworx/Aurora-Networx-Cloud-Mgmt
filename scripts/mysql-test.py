#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host
                     user="cferge",       # username
                     passwd="flipz429#",     # password
                     db="ANDC1")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

# Select data from table using SQL query.
cur.execute("SELECT * FROM andc1_hosts")

# print the first and second columns
for row in cur.fetchall() :
    print row[0], " ", row[1], " ", row[2], " "
