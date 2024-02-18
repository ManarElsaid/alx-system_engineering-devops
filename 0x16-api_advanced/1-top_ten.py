#!/usr/bin/python3
"""  a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """
    a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit
    """
    if subreddit is None:
        print("None")

    try:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
        response = requests.get(url, headers=user_agent, params={'limits': 10})
        my_data = response.json().get('data').get('children')
        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
