#!/usr/bin/python3
"""
This script sends a GET request and prints the response body
if the request fails an error code is printed instead
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    status = response.status_code
    if status >= 400:
        print("Error code:", status)
    else:
        print(response.text)
