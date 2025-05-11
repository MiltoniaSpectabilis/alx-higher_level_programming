#!/usr/bin/python3
"""This module prints all states that start with N
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
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
    cursor.execute(
        """
        SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC
        """)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
