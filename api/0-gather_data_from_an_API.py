"""
Python Script that uses the jsonplaceholder REST API
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    user_id = argv[1]
    r_user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    )
    r_todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    )

    tasks = r_todos.json()
    completed_tasks_titles = [
        task["title"] for task in tasks if task["completed"]
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            r_user.json()["name"], len(completed_tasks_titles), len(tasks)
        )
    )

    for title in completed_tasks_titles:
        print("\t {}".format(title))
