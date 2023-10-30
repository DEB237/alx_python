#!/usr/bin/python3
"""
Python script to export all employees data to a JSON file.
"""

import json
import requests
import sys


def export_employees_data_json():
    employees_ids = [
        employee["id"]
        for employee in requests.get(
            "https://jsonplaceholder.typicode.com/users/"
        ).json()
    ]
    employees_data = {}

    for id in employees_ids:
        tasks = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        ).json()
        employees_data[str(id)] = [
            {
                "username": requests.get(
                    "https://jsonplaceholder.typicode.com/users/{}".format(id)
                ).json()["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in tasks
        ]
    with open("todo_all_employees.json", "w", encoding="UTF8", newline="") as f:
        json.dump(employees_data, f)

if __name__ == "__main__":
    export_employees_data_json()
