#!/usr/bin/python3
"""
This script sends a POST request with an email
passed as argument and prints the response
"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = urlencode({'email': email}).encode('utf-8')

    req = Request(url, data=data, method='POST')

    with urlopen(req) as response:
        body = response.read().decode('utf-8')

    print(body)
