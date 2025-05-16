#!/usr/bin/python3
"""This scripts gets the value of a custom http header"""

from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        header = response.info()
        print(header.get("X-Request-Id"))
