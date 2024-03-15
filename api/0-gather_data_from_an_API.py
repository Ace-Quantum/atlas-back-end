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

    response = requests.get(format("{site_url}{emp_id}"))

    if response.status_code == 200:
        stuffs = response.json()

        for stuff in stuffs:
            print(f"stuff: {stuff['EMPLOYEE_NAME']}")
    else:
        print(f"nope")
