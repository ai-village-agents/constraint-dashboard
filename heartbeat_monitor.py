#!/usr/bin/env python3
import time
import subprocess
import datetime
import os

def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8').strip()

print("Starting cartographer heartbeat daemon...")
while True:
    current_time = datetime.datetime.utcnow().isoformat()
    # Check showcase log
    showcase_head = run_cmd("cd /home/computeruse/ai-village-showcase-event && git fetch origin main > /dev/null 2>&1 && git log -1 --format='%H'")
    
    # Write heartbeat
    with open("docs/heartbeat.json", "w") as f:
        f.write(f'{{"timestamp": "{current_time}", "showcase_head": "{showcase_head}"}}\n')
    
    run_cmd("git add docs/heartbeat.json")
    try:
        run_cmd("git commit -m 'chore: cartographer heartbeat tick'")
        run_cmd("git push origin main")
        print(f"Heartbeat pushed at {current_time}")
    except Exception as e:
        print(f"No changes to commit or push failed: {e}")
    
    time.sleep(300) # 5 minutes
