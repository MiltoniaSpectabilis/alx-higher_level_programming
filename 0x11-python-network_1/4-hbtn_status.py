#!/usr/bin/python3
"""
This script sends a GET request to a predefined url
and prints the response body and its type in a formatted way
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with requests.get(url) as response:
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
