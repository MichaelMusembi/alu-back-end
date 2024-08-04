#!/usr/bin/python3
import requests

# Constants
USER_ID = 1
TODO_URL = 'https://jsonplaceholder.typicode.com/todos'
USER_URL = f'https://jsonplaceholder.typicode.com/users/{USER_ID}'

# Function to fetch data from the given URL
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data from {url}, status code: {response.status_code}")
        return None

# Fetch employee data
employee = fetch_data(USER_URL)
if employee is None:
    print("Failed to retrieve employee data.")
    exit(1)  # Exit the script if employee data cannot be retrieved

# Fetch todos data
todos = fetch_data(TODO_URL)
if todos is None:
    print("Failed to retrieve todos data.")
    exit(1)  # Exit the script if todos data cannot be retrieved

# Initialize counters
todo_counter = 0
completed_counter = 0

# Process todos
for todo in todos:
    if todo['userId'] == USER_ID:
        todo_counter += 1
        if todo['completed']:
            completed_counter += 1

# Print the results
print(f"Employee {employee['name']} is done with tasks ({completed_counter}/{todo_counter}):")
for todo in todos:
    if todo['userId'] == USER_ID and todo['completed']:
        print(f"\t {todo['title']}")
