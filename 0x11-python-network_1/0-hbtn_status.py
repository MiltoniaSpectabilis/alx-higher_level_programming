#!/usr/bin/python3
"""Script to fetch and display status from a specific URL."""

import urllib.request

URL = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":

    """Fetch URL and print response details."""
    with urllib.request.urlopen(URL) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
