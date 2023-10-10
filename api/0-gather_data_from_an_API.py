import csv
from typing import List
import requests
import sys


def get_employee_info(employee_id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    return response.json()


def get_todo_list(employee_id: int) -> List[dict]:
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()


def export_to_csv(employee_id: int) -> None:
    employee_info = get_employee_info(employee_id)
    todo_list = get_todo_list(employee_id)

    employee_name = employee_info.get('name', 'Unknown')

    file_name = f"{employee_id}.csv"
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_list:
            task_id = task['id']
            task_title = task['title']
            task_completed = str(task['completed'])
            writer.writerow([employee_id, employee_name, task_completed, task_title])

    num_total_tasks = len(todo_list)
    print(f"Number of tasks in CSV: {num_total_tasks} - OK")
    print(f"Data exported to {file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
