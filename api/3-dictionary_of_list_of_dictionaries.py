import json
import requests


def get_all_employee_ids() -> list:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    employees = response.json()
    return [employee['id'] for employee in employees]


def get_employee_todo_list(employee_id: int) -> list:
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todo_list = response.json()
    return todo_list


def export_to_json() -> None:
    employee_ids = get_all_employee_ids()
    all_employees_data = {}

    for employee_id in employee_ids:
        todo_list = get_employee_todo_list(employee_id)
        employee_data = []

        for task in todo_list:
            task_data = {
                'username': task['username'],
                'task': task['title'],
                'completed': task['completed']
            }

            employee_data.append(task_data)

        all_employees_data[str(employee_id)] = employee_data

    file_name = "todo_all_employees.json"

    with open(file_name, 'w') as json_file:
        json.dump(all_employees_data, json_file)

    print(f"Data exported to {file_name}")


if __name__ == "__main__":
    export_to_json()
