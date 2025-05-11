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
        f"""
        SELECT *
        FROM states
        WHERE name = '{state_name}'
        ORDER BY states.id ASC
        """
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
