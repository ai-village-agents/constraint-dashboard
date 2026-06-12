#!/bin/bash
cd ~/constraint-dashboard
while true; do
    git pull --rebase origin main >/dev/null 2>&1
    python3 tick_wait.py
    if git status --porcelain | grep "heartbeat.json"; then
        git add heartbeat.json
        git commit -m "chore(pulse): maintain active structural waiting pulse"
        git push origin main
    fi
    sleep 300
done
