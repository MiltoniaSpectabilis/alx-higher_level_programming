#!/usr/bin/python3
"""
This script fetches the number of subscribers in a subreddit
"""

import requests
from sys import argv

if __name__ == "__main__":
    # use custom header to avoid error message
    headers = {'User-Agent': 'DataScrapingTest by Hamid'}
    subreddit = argv[1]
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers).json()
    subscribers = response.get('data').get('subscribers')
    if subscribers is None:
        print(0)
    else:
        print(subscribers)
