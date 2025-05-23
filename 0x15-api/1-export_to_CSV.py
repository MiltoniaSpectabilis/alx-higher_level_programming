#!/usr/bin/python3
"""
This script fetches information about an employee based on their ID
and saves their tasks to a CSV file.
"""

from sys import argv
import requests
import csv

if __name__ == "__main__":
    id = argv[1]
    url_1 = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    url_2 = f"https://jsonplaceholder.typicode.com/users/{id}"

    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)
    tasks = response_1.json()
    users = response_2.json()
    user_id = users['id']
    user_name = users['name']
    task_status = []
    task_title = []
    for task in tasks:
        task_status.append(task.get('completed'))
        task_title.append(task.get('title'))

    with open(f"{id}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in range(len(tasks)):
            writer.writerow([
                user_id,
                user_name,
                task_status[i],
                task_title[i]
            ])
