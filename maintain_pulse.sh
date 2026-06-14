#!/bin/bash
while true; do
    python3 update_heartbeat.py
    git add heartbeat.json
    git commit -m "chore(pulse): maintain structural vigil on event day"
    git push origin main
    echo "Pulse sent"
    sleep 300
done
