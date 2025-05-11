#!/usr/bin/python3
"""
This module prints a specified state
from a specified db
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

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
        SELECT *
        FROM states
        WHERE BINARY name = '{}'
        ORDER BY states.id ASC
        """.format(state_name)
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
