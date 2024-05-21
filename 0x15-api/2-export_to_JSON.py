#!/usr/bin/python3
"""Python script to export data in the JSON format -- Export to JSON task"""
import json
import requests
import sys

if __name__ == "__main__":
    id_ = int(sys.argv[1])

    url_usr_ = f"https://jsonplaceholder.typicode.com/users/{id_}"
    url_tds_ = f"https://jsonplaceholder.typicode.com/todos?userId={id_}"

    res_usr_ = requests.get(url_usr_)
    data_usr_ = res_usr_.json()

    res_tds_ = requests.get(url_tds_)
    data_tds_ = res_tds_.json()

    emp_name_ = data_usr_.get('name')
    user_id_ = data_usr_.get('id')
    name_usr_ = data_usr_.get('username')

    tasks_ = []
    for t in data_tds_:
        task_finished_ = "True" if t.get('completed') else "False"
        task = {"task": t.get('title'), "\
completed": task_finished_, "username": name_usr_}
        tasks_.append(task)

    file_ = f"{user_id_}.json"
    with open(file_, 'w') as json_file:
        json.dump({str(user_id_): tasks_}, json_file)
