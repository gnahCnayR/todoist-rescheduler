#!/bin/bash
cd /Users/ryanchang/Developer/todoist-rescheduler
export $(grep -v '^#' .env | xargs)
python3 rescheduler.py >> cron.log 2>&1
