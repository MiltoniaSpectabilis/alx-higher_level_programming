#!/usr/bin/python3

import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
database = argv[3]

connection = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM states")
for row in cursor.fetchall():
    print(row)
cursor.close()
connection.close()
