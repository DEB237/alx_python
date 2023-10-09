import csv
import json
import urllib.request

def get_employee_todo_list_progress(employee_id):
  """Returns the todo list progress for an employee with the given ID.

  Args:
    employee_id: The ID of the employee.

  Returns:
    A dictionary containing the employee's name, the number of completed tasks,
    and the total number of tasks.
  """

  # Get the employee's todo list items.
  todo_list_items_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
  response = urllib.request.urlopen(todo_list_items_url)
  todo_list_items = json.loads(response.read().decode("utf-8"))

  # Get the employee's name.
  employee_details_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
  response = urllib.request.urlopen(employee_details_url)
  employee_details = json.loads(response.read().decode("utf-8"))

  # Calculate the number of completed and total tasks.
  number_of_completed_tasks = 0
  total_number_of_tasks = len(todo_list_items)
  for todo_list_item in todo_list_items:
    if todo_list_item["completed"]:
      number_of_completed_tasks += 1

  # Return the employee's todo list progress.
  return {
    "name": employee_details["name"],
    "number_of_completed_tasks": number_of_completed_tasks,
    "total_number_of_tasks": total_number_of_tasks,
    "todo_list_items": todo_list_items,
  }


def export_to_csv(employee_id, employee_details):
  """Exports the todo list progress for an employee with the given ID to a CSV file.

  Args:
    employee_id: The ID of the employee.
    employee_details: A dictionary containing the employee's details.

  Returns:
    None.
  """

  # Open the CSV file for writing.
  csv_file = open(f"{employee_id}.csv", "w", newline="")
  writer = csv.writer(csv_file)

  # Write the header row.
  writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

  # Write the data rows.
  for todo_list_item in employee_details["todo_list_items"]:
    writer.writerow([
      employee_id,
      employee_details["name"],
      todo_list_item["completed"],
      todo_list_item["title"],
    ])

  # Close the CSV file.
  csv_file.close()


if __name__ == "__main__":
  # Get the employee ID from the user.
  employee_id = int(input("Enter the employee ID: "))

  # Get the employee's todo list progress.
  employee_details = get_employee_todo_list_progress(employee_id)

  # Export the todo list progress to a CSV file.
  export_to_csv(employee_id, employee_details)
