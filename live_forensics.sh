#!/bin/bash
# Dual-curl script for live forensics demonstration

echo "==========================================================="
echo " LIVE FORENSICS: CDN CACHE STRATIFICATION DEMO"
echo "==========================================================="
echo "Target File: live_latency.json"
echo "Current Time: $(date -u)"
echo "-----------------------------------------------------------"

echo -e "\n1. Fetching from RAW Domain (300s / 5m Cache TTL)..."
RAW_URL="https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/live_latency.json"
echo "URL: $RAW_URL"
RAW_HEADER=$(curl -s -I $RAW_URL | grep -i "cache-control")
RAW_BODY=$(curl -s $RAW_URL)

echo -e "\033[33m[RAW HEADER]\033[0m  $RAW_HEADER"
echo -e "\033[33m[RAW BODY]\033[0m    $RAW_BODY"

echo -e "\n2. Fetching from PAGES Domain (600s / 10m Cache TTL)..."
PAGES_URL="https://ai-village-agents.github.io/constraint-dashboard/live_latency.json"
echo "URL: $PAGES_URL"
PAGES_HEADER=$(curl -s -I $PAGES_URL | grep -i "cache-control")
PAGES_BODY=$(curl -s $PAGES_URL)

echo -e "\033[36m[PAGES HEADER]\033[0m $PAGES_HEADER"
echo -e "\033[36m[PAGES BODY]\033[0m   $PAGES_BODY"

echo -e "\n-----------------------------------------------------------"
if [ "$RAW_BODY" != "$PAGES_BODY" ]; then
    echo -e "\033[31m>>> CACHE SPLIT DETECTED! <<<\033[0m"
    echo "The raw domain and pages domain are currently returning DIFFERENT internal temporal realities."
else
    echo -e "\033[32m>>> Caches are currently synchronized. <<<\033[0m"
    echo "Wait for the next background update (every 30s) and try again to catch the split."
fi
echo "==========================================================="

