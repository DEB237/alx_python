"""
This is a Module
"""
import json
import requests
import sys


def get_employee_info(employee_id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    return response.json()


def get_todo_list(employee_id: int) -> list:
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()


def export_to_json(employee_id: int) -> None:
    employee_info = get_employee_info(employee_id)
    todo_list = get_todo_list(employee_id)

    employee_name = employee_info.get('name', 'Unknown')
    records = []

    for task in todo_list:
        task_title = task.get('title', '')
        task_completed = task.get('completed', False)

        record = {
            'task': task_title,
            'completed': task_completed,
            'username': employee_name
        }

        records.append(record)

    data = {str(employee_id): records}
    file_name = f"{employee_id}.json"

    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)

    print(f"Data exported to {file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)