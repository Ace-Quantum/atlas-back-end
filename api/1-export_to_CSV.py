#!/usr/bin/python3

"""
I'm documenting for the check
"""

import csv
import json
import requests
import sys
import urllib


def retrieve_to_do(emp_id):
    """
    More documentation for the check
    """
    todo_all = {}
    todo_done = []
    csv_data = []

    # fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    filename = f"{emp_id}.csv"

    # print(filename)

    site_url = "https://jsonplaceholder.typicode.com/"
    emp_url = f"{site_url}users/{emp_id}"
    to_do_url = f"{emp_url}/todos"

    # print({emp_url})

    employee_data = requests.get(emp_url)
    to_dos_data = requests.get(to_do_url)

    emp_dict = employee_data.json()
    todo_all = to_dos_data.json()

    emp_name = emp_dict.get("name")

    for task in todo_all:
        if task.get("completed") is True:
            # print(task)
            todo_done.append(task)

    print(f"Employee {emp_name} is done with tasks", end="")
    print(f"({len(todo_done)}/{len(todo_all)}):")

    for task in todo_done:
        print("\t " + task.get("title"))

    for task in todo_all:
        task_list = []
        task_list.append(emp_id)
        task_list.append(emp_dict.get("username"))
        # print(f"username: {emp_dict.get('username')}")
        task_list.append(task.get("completed"))
        task_list.append(task.get("title"))
        csv_data.append(task_list)

    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        writer.writerows(csv_data)


if __name__ == "__main__":
    retrieve_to_do(sys.argv[1])
