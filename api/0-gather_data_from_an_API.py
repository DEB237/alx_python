import requests
import sys
from typing import List


def get_employee_info(employee_id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    return response.json()


def get_todo_list(employee_id: int) -> List[dict]:
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()


def display_todo_progress(employee_id: int) -> None:
    employee_info = get_employee_info(employee_id)
    todo_list = get_todo_list(employee_id)

    num_total_tasks = len(todo_list)
    num_completed_tasks = sum(1 for task in todo_list if task['completed'])

    employee_name = employee_info.get('name', 'Unknown')

    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{num_total_tasks}):")

    for task in todo_list:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_todo_progress(employee_id)