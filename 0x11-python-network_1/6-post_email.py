#!/usr/bin/python3
"""
This script sends a POST request with an email as a param
and then prints the response
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    response = requests.post(url, data)
    print(response.text)
