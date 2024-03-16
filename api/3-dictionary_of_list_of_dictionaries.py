#!/usr/bin/python3

"""
documentation for the check
"""

import json
import requests


def retrieve_to_do():
    """
    more documentation
    """

    todo_all = {}
    export_dict = {}
    task_list = []
    temp_dict = {}
    filepath = "todo_all_employees.json"

    site_url = "https://jsonplaceholder.typicode.com/"
    emps_url = f"{site_url}users"

    all_emps = requests.get(emps_url)

    all_emp_dict = all_emps.json()

    # print(all_emp_dict)
    # print("I am slowly losing my will to live")
    for emp in all_emp_dict:
        # print({emp['id']})
        # print({emp['name']})
        emp_id = emp.get("id")
        todo_url = f"{emps_url}/{emp_id}/todos"
        todo_all = requests.get(todo_url)
        todo_all_dict = todo_all.json()
        for todo in todo_all_dict:
            # print(todo)
            # print({todo['userId']})
            # print({todo['title']})
            temp_dict['username'] = emp.get('username')
            temp_dict['task'] = todo.get('title')
            temp_dict['completed'] = todo.get('completed')
            task_list.append(temp_dict)
            temp_dict = {}
        export_dict[emp_id] = task_list

    with open(filepath, "w") as f:
        json.dump(export_dict, f)


if __name__ == "__main__":
    retrieve_to_do()
