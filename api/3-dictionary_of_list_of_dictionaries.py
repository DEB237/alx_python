"""
This is a Module
"""
import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    try:
        todos_response = requests.get(todos_url)
        user_response = requests.get(user_url)
        todos_response.raise_for_status()
        user_response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f'Error: {err}')
        sys.exit(1)

    todos = todos_response.json()
    user = user_response.json()

    completed_tasks = [{"task": todo['title'], "completed": todo['completed'], "username": user['name']} for todo in todos]

    data = {employee_id: completed_tasks}

    with open(f"todo_all_employee.json", mode='a', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False))
    
    print(f"Data has been exported to todo_all_employee.json")
