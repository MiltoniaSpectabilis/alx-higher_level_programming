#!/usr/bin/python3
"""
This module prints all the cities from a specified state
"""

from MySQLdb import connect, cursors
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]
    connection = connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )
    cursor = connection.cursor(cursorclass=cursors.DictCursor)
    query = """
    SELECT cities.name
    FROM states
    JOIN cities
    ON state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state,))
    cities = [city['name'] for city in cursor]
    print(", ".join(cities))
