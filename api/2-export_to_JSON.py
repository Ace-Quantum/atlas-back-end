#!/usr/bin/python3

"""
I'm documenting for the check
"""

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
    json_dict = {}
    json_in_dict = []
    json_in_dict_in_dict = {}
    filepath = f"{emp_id}.json"

    site_url = "https://jsonplaceholder.typicode.com/"
    emp_url = f"{site_url}users/{emp_id}"
    to_do_url = f"{emp_url}/todos"

    employee_data = requests.get(emp_url)
    to_dos_data = requests.get(to_do_url)

    emp_dict = employee_data.json()
    todo_all = to_dos_data.json()

    emp_name = emp_dict.get("name")
    # print(emp_dict.get("username"))

    for task in todo_all:
        if task.get("completed") is True:
            todo_done.append(task)

    print(f"Employee {emp_name} is done with tasks", end="")
    print(f"({len(todo_done)}/{len(todo_all)}):")

    # print(emp_dict.get("username"))

    for task in todo_done:
        print("\t " + task.get("title"))

    # print(emp_dict.get("username"))

    for task in todo_all:
        # print(emp_dict.get("username"))
        # print(f"task: {task.get('title')}, status: {task.get('completed')}, username: {task.get('username')}")
        json_in_dict_in_dict["task"] = task.get("title")
        json_in_dict_in_dict["completed"] = task.get("completed")
        json_in_dict_in_dict["username"] = emp_dict.get("username")
        json_in_dict.append(json_in_dict_in_dict)

    # print(json_in_dict)

    json_dict[emp_id] = json_in_dict

    with open(filepath, "w") as f:
        json.dump(json_dict, f)


if __name__ == "__main__":
    retrieve_to_do(sys.argv[1])
