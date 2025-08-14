# Todoist Rescheduler Script
i got tired of rescheduling tasks every morning, so this repo automatically reschedules overdue todoist tasks every day. 

for my personal use, but feel free to use!

---
how to use:
1. clone the repo (make sure to change file paths to your own)

2. set up your API key
create an .env file and add this 
```
TODOIST_API_KEY=your_api_key_here
```

3. install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. (optional) run the script to test
```bash
python3 rescheduler.py
```

run with github actions:

1. **Clone this repo and push to GitHub**

2. **Add your Todoist API key as a GitHub secret:**

3. **Enable GitHub Actions:**

4. **Test the workflow:**

The workflow will run daily at 8:05 AM UTC (12:05 AM PST or 1:05 AM PST) and automatically reschedule your overdue tasks.

<!-- to run everyday (mac only):
1. create launchd job (adjust name as needed)
```bash
nano ~/Library/LaunchAgents/com.ryanchang.todoistrescheduler.plist
```

2. paste this: this will run the script once everyday (adjust repo name as needed)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
   "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>com.ryanchang.todoistrescheduler</string>

    <key>ProgramArguments</key>
    <array>
      <string>/Users/ryanchang/Developer/todoist-rescheduler/run_rescheduler.sh</string>
    </array>

    <key>StartInterval</key>
    <integer>21600</integer>

    <key>RunAtLoad</key>
    <true/>

    <key>StandardOutPath</key>
    <string>/Users/ryanchang/Developer/todoist-rescheduler/launchd.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/ryanchang/Developer/todoist-rescheduler/launchd.log</string>
  </dict>
</plist>
```

3. load the job
```bash
launchctl load ~/Library/LaunchAgents/com.ryanchang.todoistrescheduler.plist
```

4. confirm it worked:
```bash
launchctl list | grep todoist
```

 -->
