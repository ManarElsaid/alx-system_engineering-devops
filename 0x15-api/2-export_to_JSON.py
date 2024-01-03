#!/usr/bin/python3
""" Python script to export data in the json format."""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    employee_id = sys.argv[1]

    url = base_url + "/" + employee_id

    response = requests.get(url)
    employee_name = response.json().get("username")

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    records = {employee_id: []}
    for task in tasks:
        records[employee_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name})
    with open("{}.json".format(employee_id), "w") as file:
        json.dump(records, file)
