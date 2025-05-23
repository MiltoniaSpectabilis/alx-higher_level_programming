#!/usr/bin/python3
"""
This module prints all cities with their corresponding states
"""

from MySQLdb import connect
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    connection = connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )
    cursor = connection.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM states
    JOIN cities
    ON states.id = cities.state_id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
