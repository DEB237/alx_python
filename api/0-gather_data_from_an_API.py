import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python todo.py <employee_id>')
        sys.exit(1)

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

    completed_tasks = [todo for todo in todos if todo['completed']]
    NUMBER_OF_DONE_TASKS = len(completed_tasks)
    TOTAL_NUMBER_OF_TASKS = len(todos)

    EMPLOYEE_NAME = user['name']

    print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for task in completed_tasks:
        TASK_TITLE = task['title']
        print(f"\t{TASK_TITLE}")
