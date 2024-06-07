#!/usr/bin/python3
"""function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
--Recurse it Task"""
import requests


def recurse(subreddit, hot_list=[]):
    "recurse function"
    url_ = f"https://www.reddit.com/r/{subreddit}/hot.json"
    hdrs_ = {'User-Agent': 'Custom User Agent'}
    param_s_ = {}
    if hot_list:
        last_post = hot_list[-1]
        param_s_['after'] = last_post['name']

    res_ = requests.get(url_, headers=hdrs_, params=param_s_)

    if res_.status_code == 200:
        dat_ = res_.json()
        pub_ = dat_.get('data', {}).get('children', [])
        hot_list.extend(pub_)

        if len(hot_list) >= 10 or not pub_:
            return [a['data']['title'] for a in hot_list[:10]]
        else:
            return recurse(subreddit, hot_list)
    else:
        return None
