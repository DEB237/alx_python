import json
import urllib.request

def get_employee_todo_list_progress(employee_id):
  """Returns the todo list progress for an employee with the given ID.

  Args:
    employee_id: The ID of the employee.

  Returns:
    A dictionary containing the employee's name, the number of completed tasks, and
    the total number of tasks.
  """

  # Get the employee's todo list items.
  todo_list_items_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
  response = urllib.request.urlopen(todo_list_items_url)
  todo_list_items = json.loads(response.read().decode("utf-8"))

  # Get the employee's name.
  employee_details_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
  response = urllib.request.urlopen(employee_details_url)
  employee_details = json.loads(response.read().decode("utf-8"))

  # Check if the employee exists.
  if not employee_details:
    raise Exception("Employee does not exist.")

  # Check if the employee has a name.
  if not employee_details["name"]:
    raise Exception("Employee does not have a name.")

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
  }


def main():
  # Get the employee ID from the user.
  employee_id = int(input("Enter the employee ID: "))

  # Get the employee's todo list progress.
  try:
    todo_list_progress = get_employee_todo_list_progress(employee_id)
  except Exception as e:
    print(e)
    exit(1)

  # Display the employee's todo list progress on the standard output.
  print(f"Employee {todo_list_progress['name']} is done with tasks({todo_list_progress['number_of_completed_tasks']}/{todo_list_progress['total_number_of_tasks']}):")
  for todo_list_item in todo_list_progress["todo_list_items"]:
    if todo_list_item["completed"]:
      print(f"\t{todo_list_item['title']}")


if __name__ == "__main__":
  main()
