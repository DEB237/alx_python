import csv
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


def export_to_csv(employee_id: int) -> None:
    employee_info = get_employee_info(employee_id)
    todo_list = get_todo_list(employee_id)

    employee_name = employee_info.get('name', 'Unknown')

    file_name = f"{employee_id}.csv"

    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_list:
            task_id = task.get('id', '')
            task_title = task.get('title', '')
            task_completed = task.get('completed', False)

            writer.writerow([task_id, employee_name, str(task_completed), task_title])

    print(f"Data exported to {file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)