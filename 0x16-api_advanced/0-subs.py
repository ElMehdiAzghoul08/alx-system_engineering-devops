#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of sub_s_
--How many subs task"""
import requests


def number_of_subscribers(subreddit):
    "number_of_subscribers function"
    url_ = f"https://www.reddit.com/r/{subreddit}/about.json"
    hdrs_ = {'User-Agent': 'Custom User Agent'}
    res_ = requests.get(url_, headers=hdrs_)

    if res_.status_code == 200:
        dat_ = res_.json()
        sub_s_ = dat_['data']['subscribers']
        return sub_s_
    else:
        return 0
