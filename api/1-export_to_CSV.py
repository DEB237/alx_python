import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID")
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

    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([employee_id, EMPLOYEE_NAME, todo['completed'], todo['title']])
    
    print(f"Data has been exported to {employee_id}.csv")
