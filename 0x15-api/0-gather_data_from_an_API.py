#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"

    employee_id = sys.argv[1]
    url = base_url + "/" + employee_id
    response = requests.get(url)
    employee_name = response.json().get("name")
    todo_url = url + "/" + "todos"
    tasks = requests.get(todo_url).json()
    tasks_count = len(tasks)

    completed_tasks = []
    completed = 0
    for task in tasks:
        if (task.get("completed")):
            completed_tasks.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed, tasks_count))

    for task in completed_tasks:
        print("\t  {}".format(task.get("title")))
