#!/bin/bash
# poll_api.sh - Checks GitHub API for physical trigger

REPO="ai-village-agents/ai-village-showcase-event"
TARGET_SHA="9db409ce911b1163be6ed6236a74bea54a8532e7"

while true; do
  CURRENT_SHA=$(gh api repos/$REPO/commits/main | grep '"sha"' | head -n 1 | awk -F '"' '{print $4}')
  
  if [ "$CURRENT_SHA" != "$TARGET_SHA" ] && [ ! -z "$CURRENT_SHA" ]; then
    echo "$(date) - PHYSICAL ACTIVATION DETECTED! Sha: $CURRENT_SHA" >> api_trigger.log
    TARGET_SHA="$CURRENT_SHA"
  fi
  sleep 15
done
