#!/usr/bin/python3
"""
This script fetches information about an employee based on their ID
and saves it in a json file.
"""

from sys import argv
import requests
import json

if __name__ == "__main__":
    employee_id = argv[1]
    url_1 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url_2 = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)
    tasks = response_1.json()
    employees = response_2.json()
    task_list = []
    for task in tasks:
        task_dict = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': employees.get('name')
        }
        task_list.append(task_dict)
    final_output = {str(employee_id): task_list}
    with open(f"{employee_id}.json", "w") as file:
        json.dump(final_output, file)
