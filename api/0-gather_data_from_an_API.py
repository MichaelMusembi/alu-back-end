import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        # Replace 'API_BASE_URL' with the actual API base URL
        API_BASE_URL = "https://jsonplaceholder.typicode.com"
        
        # Fetch employee information
        user_response = requests.get(f"{API_BASE_URL}/users/{employee_id}")
        if user_response.status_code != 200:
            print(f"Error: Unable to fetch employee information for ID {employee_id}")
            return
        
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Fetch TODO list for the employee
        todos_response = requests.get(f"{API_BASE_URL}/todos", params={"userId": employee_id})
        if todos_response.status_code != 200:
            print(f"Error: Unable to fetch TODO list for employee ID {employee_id}")
            return

        todos_data = todos_response.json()

        # Calculate number of completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task['completed']]
        number_of_done_tasks = len(completed_tasks)

        # Print the TODO list progress
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
