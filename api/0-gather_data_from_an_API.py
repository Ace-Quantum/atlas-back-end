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
    emp_to_do_all = {}
    emp_to_do_done = []

    site_url = "https://jsonplaceholder.typicode.com/"
    emp_url = f"{site_url}users/{emp_id}"
    to_do_url = f"{emp_url}/todos"

    # print({emp_url})

    employee_data = requests.get(emp_url)
    to_dos_data = requests.get(to_do_url)

    emp_dict = employee_data.json()
    emp_to_do_all = to_dos_data.json()

    emp_name = emp_dict.get("name")

    for task in emp_to_do_all:
        if task.get("completed") is True:
            # print(task)
            emp_to_do_done.append(task)

    print(f"Employee {emp_name} is done with tasks(
          {len(emp_to_do_done)}/{len(emp_to_do_all)}):")

    for task in emp_to_do_done:
        print("  " + task.get("title"))


if __name__ == "__main__":
    retrieve_to_do(sys.argv[1])
