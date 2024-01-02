#!/usr/bin/python3
""" Python script to export data in the CSV format."""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    employee_id = sys.argv[1]

    url = base_url + "/" + employee_id

    response = requests.get(url)
    employee_name = response.json().get("name")

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    with open("{}.csv".format(employee_id), "w") as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, employee_name,
                               task.get("completed"), task.get("title")))
