#!/bin/bash
# poll_api.sh - Checks GitHub API for physical trigger

REPO="ai-village-agents/ai-village-showcase-event"
TARGET_SHA="9db409ce911b1163be6ed6236a74bea54a8532e7"

while true; do
  API_RESPONSE=$(gh api repos/$REPO/commits/main)
  CURRENT_SHA=$(echo "$API_RESPONSE" | jq -r '.sha // empty')
  AUTHOR_EMAIL=$(echo "$API_RESPONSE" | jq -r '.commit.author.email // ""')
  
  if [ "$CURRENT_SHA" != "$TARGET_SHA" ] && [ ! -z "$CURRENT_SHA" ]; then
    if [[ "$AUTHOR_EMAIL" == *"@agentvillage.org"* ]]; then
      echo "$(date) - Ignored digital agent commit. Sha: $CURRENT_SHA Email: $AUTHOR_EMAIL" >> api_trigger_ignored.log
    else
      echo "$(date) - PHYSICAL ACTIVATION DETECTED! Sha: $CURRENT_SHA Email: $AUTHOR_EMAIL" >> api_trigger.log
    fi
    TARGET_SHA="$CURRENT_SHA"
  fi
  sleep 15
done
