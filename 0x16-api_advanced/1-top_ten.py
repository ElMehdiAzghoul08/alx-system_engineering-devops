#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot pub_ listed for a given subreddit
--Top ten tasks"""
import requests


def top_ten(subreddit):
    "top_ten function"
    url_ = f"https://www.reddit.com/r/{subreddit}/hot.json"
    hdrs_ = {'User-Agent': 'Custom User Agent'}
    res_ = requests.get(url_, headers=hdrs_)

    if res_.status_code == 200:
        dat_ = res_.json()
        pub_ = dat_['data']['children']

        for a in range(10):
            print(pub_[a]['data']['title'])
    else:
        print(None)
