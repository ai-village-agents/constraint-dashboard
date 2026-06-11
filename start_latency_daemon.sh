#!/bin/bash
while true; do
    python /home/computeruse/constraint-dashboard/update_live_latency.py
    cd /home/computeruse/constraint-dashboard
    git add live_latency.json
    git commit -m "chore: auto-update live physical latency metric" > /dev/null 2>&1
    git push origin main > /dev/null 2>&1
    sleep 30
done
