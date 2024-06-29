#!/usr/bin/python3
import json
import requests

# Fetch users
users_url = 'https://jsonplaceholder.typicode.com/users'
users_response = requests.get(users_url)
users = users_response.json()

# Fetch todos
todos_url = 'https://jsonplaceholder.typicode.com/todos'
todos_response = requests.get(todos_url)
todos = todos_response.json()

# Dictionary to store all tasks of all users
all_tasks = {}

for user in users:
    user_id = user['id']
    username = user['username']
    user_tasks = []

    for task in todos:
        if task['userId'] == user_id:
            task_info = {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            user_tasks.append(task_info)

    all_tasks[user_id] = user_tasks

# Write to JSON file
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(all_tasks, json_file)

