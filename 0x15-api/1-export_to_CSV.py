#!/usr/bin/python3
"""Python script to export data in the CSV format --Export to CSV task"""
import csv
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

    file_ = f"{user_id_}.csv"

    with open(file_, 'w', newline='') as file_csv_:
        w_csv_ = csv.writer(file_csv_, quoting=csv.QUOTE_ALL)
        w_csv_.writerow(['USER_ID', 'USERNAME', '\
TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        for t in data_tds_:
            task_finished_ = "True" if t.get('completed') else "False"
            w_csv_.writerow([user_id_, name_usr_, task_finished_, t.get('\
title')])
