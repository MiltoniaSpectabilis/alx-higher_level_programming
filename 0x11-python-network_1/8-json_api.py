#!/usr/bin/python3
"""
This script sends a POST request with a letter
and returns the response body
"""

from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    try:
        response = requests.post(url, data=data)
        json_data = response.json()
        if json_data:
            print(f"{[json_data['id']]} {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
