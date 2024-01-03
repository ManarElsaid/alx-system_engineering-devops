#!/usr/bin/python3
""" Python script to export data in the json format."""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()
    records = {}
    for user in users:
        user_id = user.get("id")
        user_name = user.get("username")
        todo_url = url + "/" + str(user_id) + "/todos/"
        response = requests.get(todo_url)
        tasks = response.json()
        records[user_id] = []
        for task in tasks:
            records[user_id].append({
                "username": user_name,
                "task": task.get("title"),
                "completed": task.get("completed")})
    with open('todo_all_employees.json', 'w') as file:
        json.dump(records, file)
