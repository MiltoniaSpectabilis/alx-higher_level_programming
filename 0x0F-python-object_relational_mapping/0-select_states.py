#!/usr/bin/python3
"""This module lists all states from a specified database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
