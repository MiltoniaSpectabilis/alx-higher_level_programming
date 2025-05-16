#!/usr/bin/python3
"""
This script tries to send a request and print the response
if the request fails an error code is printed instead
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    try:
        with urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print("Error code:", e.getcode())
