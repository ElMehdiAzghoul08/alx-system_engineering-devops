#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress --Gather data from api t
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <id_>")
    else:
        try:
            id_ = int(sys.argv[1])

            url_usr_ = f"https://jsonplaceholder.typicode.com/users/{id_}"
            url_tds_ = f"https://jsonplaceholder.typicode.com/todos?\
                    userId={id_}"

            res_usr_ = requests.get(url_usr_)
            data_usr_ = res_usr_.json()

            res_tds_ = requests.get(url_tds_)
            data_tds_ = res_tds_.json()

            emp_name_ = data_usr_.get('name')

            tot_tasks_ = len(data_tds_)
            tasks_finished_ = [t for t in data_tds_ if t.get('completed')]
            num_tasks_finished_ = len(tasks_finished_)

            print(f"Employee {emp_name_} is done with tasks(\
                    {num_tasks_finished_}/{tot_tasks_}):")
            for t in tasks_finished_[:11]:
                print(f"\t {t.get('title')}")

        except ValueError:
            print("The employee ID must be an integer.")
