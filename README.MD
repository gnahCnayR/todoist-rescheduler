# Todoist Rescheduler Script
i got tired of rescheduling tasks every morning, so this repo automatically reschedules overdue todoist tasks every day. 

for my personal use, but feel free to use!

---
how to use:
1. clone the repo

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

to run everyday:
1. open crontab
```bash
crontab -e
```

2. paste this: this will run the script once everyday at 7 am
```
0 7 * * * /[path to your]/run_rescheduler.sh
```

3. enter :x to save and exit 

4. confirm it worked:
```bash
crontab -l
```


