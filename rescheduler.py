#!/usr/bin/env python3

import os
import requests
from datetime import datetime, date
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variable
API_TOKEN = os.getenv("TODOIST_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

BASE_URL = "https://api.todoist.com/API/v2"

def reschedule_overdue_tasks():
    print("Fetching tasks...")
    try:
        response = requests.get(f"{BASE_URL}/tasks", headers=HEADERS)
        response.raise_for_status()
        tasks = response.json()
        print(f"Fetched {len(tasks)} tasks.")
    except Exception as e:
        print("Failed to fetch tasks:", e)
        return
    
    today_str = date.today().isoformat()
    for idx, task in enumerate(tasks):
        due = task.get("due")

        if not due:
            continue

        if isinstance(due, str):
            due_str = due
        elif isinstance(due, dict):
            due_str = due.get("datetime") or due.get("date")
        else:
            print(f"Unexpected due format: {due}")
            continue

        try:
            due_date = datetime.fromisoformat(due_str).date()
        except Exception as e:
            print(f"Could not parse due date: {due_str} — {e}")
            continue

        if due_date < date.today():
            try:
                update_url = f"{BASE_URL}/tasks/{task['id']}"
                update_payload = {
                    "due_string": "today"
                }
                update_res = requests.post(update_url, headers=HEADERS, json=update_payload)
                update_res.raise_for_status()
                print(f"Rescheduled task '{task.get('content')}' to today.")
            except Exception as e:
                print(f"Failed to update task '{task.get('content')}':", e)
        

if __name__ == "__main__":
    reschedule_overdue_tasks()