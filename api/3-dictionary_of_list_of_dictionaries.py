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


def export_to_json(employee_todo_list_progress_dict):
  """Exports the todo list progress for all employees to a JSON file.

  Args:
    employee_todo_list_progress_dict: A dictionary containing the todo list
      progress for all employees.

  Returns:
    None.
  """

  # Create the JSON object.
  json_object = {}

  # Add the todo list progress for each employee to the JSON object.
  for employee_id, employee_todo_list_progress in employee_todo_list_progress_dict.items():
    employee_task_data = []
    for todo_list_item in employee_todo_list_progress["todo_list_items"]:
      employee_task_data.append({
        "username": employee_todo_list_progress["name"],
        "task": todo_list_item["title"],
        "completed": todo_list_item["completed"],
      })

    json_object[employee_id] = employee_task_data

  # Save the JSON object to a file.
  with open("all_employee_todo_list_progress.json", "w") as json_file:
    json.dump(json_object, json_file, indent=4)


if __name__ == "__main__":
  # Get the todo list progress for all employees.
  employee_todo_list_progress_dict = {}
  for employee_id in range(1, 11):
    employee_todo_list_progress = get_employee_todo_list_progress(employee_id)
    employee_todo_list_progress_dict[employee_id] = employee_todo_list_progress

  # Export the todo list progress for all employees to a JSON file.
  export_to_json(employee_todo_list_progress_dict)
