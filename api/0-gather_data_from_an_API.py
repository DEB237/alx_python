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
    num_completed_tasks = len(completed_tasks)
    num_total_tasks = len(todos)

    print(f"Employee {user['name']} is done with tasks({num_completed_tasks}/{num_total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")
