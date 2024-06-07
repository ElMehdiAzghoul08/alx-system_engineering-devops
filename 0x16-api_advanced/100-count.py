#!/usr/bin/python3
"""function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
--Count it Task"""
import requests


def count_words(subreddit, word_list):
    count_w_ = {}
    url_ = f"https://www.reddit.com/r/{subreddit}/hot.json"
    hdrs_ = {'User-Agent': 'Custom User Agent'}
    res_ = requests.get(url_, headers=hdrs_)

    if res_.status_code == 200:
        dat_ = res_.json()
        pub_ = dat_.get('data', {}).get('children', [])

        for a in pub_:
            nm_ = a['data']['title'].lower()
            for x in word_list:
                if nm_.count(x.lower()) > 0:
                    count_w_[x.lower()] = count_w_.get(
                            x.lower(), 0) + nm_.count(x.lower())

        count_sd_ = sorted(count_w_.items(), key=lambda x: (-x[1], x[0]))
        for x, y in count_sd_:
            print(f"{x}: {y}")
    else:
        print("Invalid")
