"""
This is a Module
"""
import json
import requests
import sys

if __name__ == 'main':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID")
        sys.exit(1)

    todos_url = f'https://jsonplaceholder.typicode.com/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users'

    try:
        todos_response = requests.get(todos_url)
        user_response = requests.get(user_url)
        todos_response.raise_for_status()
        user_response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f'Error: {err}')
        sys.exit(1)

    todos = todos_response.json()
    users = user_response.json()

    data = {}

    for user in users:
        employee_id = str(user['id'])
        username = user['name']

        employee_tasks = [
            {"task": todo['title'], "completed": todo['completed'], "username": username}
            for todo in todos
            if todo['userId'] == user['id']
        ]

        data[employee_id] = employee_tasks

    with open("todo_all_employee.json", mode='w') as file:
        json.dump(data, file)

    print("Data has been exported to todo_all_employee.json")