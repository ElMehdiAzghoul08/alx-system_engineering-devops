#!/usr/bin/python3
"""Python script to export data in the JSON format
--Dictionary of list of dictionaries task"""
import json
import requests
import sys

if __name__ == "__main__":
    id_usr_ = sys.argv[1]
    url_ = "https://jsonplaceholder.typicode.com/users/{}/tds_".format(id_usr_)

    res_ = requests.get(url_)
    tds_ = res_.json()

    all_emp_ = {}

    for td_ in tds_:
        id_usr_ = str(td_['userId'])
        name_usr_ = td_['name_usr_']
        task_ = td_['title']
        finished_ = td_['completed']

        if id_usr_ not in all_emp_:
            all_emp_[id_usr_] = []

        all_emp_[id_usr_].append({
            "username": name_usr_,
            "task": task_,
            "completed": finished_
        })

    with open('todo_all_employees.json', 'w') as file_:
        json.dump(all_emp_, file_)
