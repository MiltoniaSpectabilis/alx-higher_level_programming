#!/usr/bin/python3
"""
This script sends a GET request to fetch the first
10 commits from a given repo
"""

from sys import argv
import requests


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    json_data = response.json()
    for element in json_data[:10]:
        print(f"{element['sha']}: {element['commit']['author']['name']}")
