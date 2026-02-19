#!/usr/bin/env python3

import os
from datetime import datetime, date
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variable
API_TOKEN = os.getenv("TODOIST_API_KEY")

def reschedule_overdue_tasks():
    print("Fetching tasks...")
    try:
        api = TodoistAPI(API_TOKEN)
        
        # Collect all tasks from the paginator
        all_tasks = []
        for tasks in api.get_tasks():
            all_tasks.extend(tasks)
        
        print(f"Fetched {len(all_tasks)} tasks.")
    except Exception as e:
        print("Failed to fetch tasks:", e)
        return
    
    overdue_count = 0
    for task in all_tasks:
        if not task.due:
            continue

        # Get the due date from the task
        due_date_str = task.due.date
        if not due_date_str:
            continue

        try:
            # Parse the due date (format: YYYY-MM-DD)
            # Check if it's already a date object or a string
            if isinstance(due_date_str, str):
                due_date = datetime.fromisoformat(due_date_str).date()
            elif isinstance(due_date_str, date):
                due_date = due_date_str
            else:
                print(f"Unexpected due date type: {type(due_date_str)}")
                continue
        except Exception as e:
            print(f"Could not parse due date: {due_date_str} — {e}")
            continue

        # Check if the task is overdue
        if due_date < date.today():
            try:
                api.update_task(task_id=task.id, due_string="today")
                print(f"Rescheduled task '{task.content}' to today.")
                overdue_count += 1
            except Exception as e:
                print(f"Failed to update task '{task.content}':", e)
    
    print(f"Rescheduled {overdue_count} overdue tasks.")
        

if __name__ == "__main__":
    reschedule_overdue_tasks()