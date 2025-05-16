#!/usr/bin/python3
"""
This is a script that sends a GET request to a url
and prints the request's ID
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    headers = response.headers
    print(headers.get("X-Request-Id"))
