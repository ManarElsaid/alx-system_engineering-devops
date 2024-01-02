#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress."""
import sys
import requests


if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com/users"

    employeeId = sys.argv[1]
    url = baseUrl + "/" + employeeId
    response = requests.get(url)
    employeeName = response.json().get("name")
    todoUrl = url + "/" + "todos"
    tasks = requests.get(todoUrl).json()
    tasks_count = len(tasks)

    completed_tasks = []
    completed = 0
    for task in tasks:
        if (task.get("completed")):
            completed_tasks.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, completed, tasks_count))

    for task in completed_tasks:
        print("\t  {}".format(task.get("title")))
