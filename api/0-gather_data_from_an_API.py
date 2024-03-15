#!/usr/bin/python3

"""
I'm documenting for the check
"""

if __name__ == "__main__":
    retrieve_to_do

import json
import requests
import sys
import urllib


def retrieve_to_do(emp_id):
    """
    More documentation for the check
    """
    site_url = "https://jsonplaceholder.typicode.com/"
    emp_url = format("{site_url}/users/{emp_id}")
    to_do_url = format("{site_url}/todos")

    employee_data = requests.get(format("{emp_url}"))
    to_dos_data = requests.get(format("{to_do_url}"))

    if employee_data.status_code == 200 or to_dos_data.status_code == 200:
        employee = employee_data.json()
        to_dos = to_dos_data()

        print("{employee}")
    else:
        print(f"nope")
