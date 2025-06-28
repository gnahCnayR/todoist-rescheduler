#!/bin/bash
cd /Users/ryanchang/Developer/todoist-rescheduler

# Add a timestamp to know when it ran
echo "=== Running rescheduler at $(date) ===" >> launchd.log

# Load environment variables from .env
export $(grep -v '^#' .env | xargs)

# Run the Python script and append all output to the log
python3 rescheduler.py >> launchd.log 2>&1
