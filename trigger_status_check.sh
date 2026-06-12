#!/bin/bash
# Cartographer action script to ensure structural engagement.
echo "Checking live latency json state at $(date)"
cat live_latency.json | grep -E "status|latency_minutes"
