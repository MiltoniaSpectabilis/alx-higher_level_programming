#!/usr/bin/python3
"""
This script fetches information about an employee based on their ID
"""

from sys import argv
import requests

if __name__ == "__main__":
    id = argv[1]
    url_1 = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    url_2 = f"https://jsonplaceholder.typicode.com/users/{id}"

    response_1 = requests.get(url_1)
    tasks = response_1.json()
    num_tasks = len(tasks)
    num_done_tasks = 0
    task_names = []
    for task in tasks:
        if task['completed'] is True:
            num_done_tasks += 1
            task_names.append(task['title'])

    response_2 = requests.get(url_2)
    user = response_2.json()
    name = user['name']

    print(f"Employee {name} is done with tasks({num_done_tasks}/{num_tasks}):")
    for task_name in task_names:
        print("\t" + " " + task_name)
