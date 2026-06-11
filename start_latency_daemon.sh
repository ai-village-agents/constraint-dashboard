#!/bin/bash
while true; do
    cd /home/computeruse/ai-village-agents/constraint-dashboard
    python3 update_live_latency.py
    
    # Only try to commit if there are changes
    if ! git diff --quiet live_latency.json; then
        git stash push -m "daemon_stash" live_latency.json
        git fetch --all > /dev/null 2>&1
        git pull --rebase origin main > /dev/null 2>&1
        git stash pop > /dev/null 2>&1
        
        git add live_latency.json
        git commit -m "chore: auto-update live physical latency metric" > /dev/null 2>&1
        git push origin main > /dev/null 2>&1
    fi
    sleep 60
done
