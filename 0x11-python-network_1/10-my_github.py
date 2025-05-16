#!/usr/bin/python3
"""
This script takes github credentials and uses
the github api to display the user's 'id'
"""

from sys import argv
import requests

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    url = f"https://api.github.com/users/{username}"
    headers = {'Authorization': f'Bearer {password}'}

    response = requests.get(url, headers=headers)
    json_data = response.json()
    print(json_data.get('id'))
