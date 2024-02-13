#!/usr/bin/python3
"""
a function that queries
the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """function returns the number of subscribers of certain subreddit"""
    if subreddit is None:
        return 0
    
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
        response = requests.get(base_url, headers={'User-agent' : 'Google Chrome Version 81.0.4044.129'})
        return response.json().get('data').get('subscribers')
    except Exception:
        return 0