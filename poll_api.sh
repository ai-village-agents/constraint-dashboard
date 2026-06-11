#!/bin/bash
while true; do
  API_RESPONSE=$(gh api repos/ai-village-agents/ai-village-showcase-event/commits/main)
  SHA=$(echo "$API_RESPONSE" | jq -r '.sha')
  if [ "$SHA" != "9db409ce911bd766d3a9bb2c1f36987c805eb3ab" ]; then
    echo "$(date) - NEW COMMIT DETECTED! Sha: $SHA" >> /home/computeruse/constraint-dashboard/api_trigger.log
  fi
  sleep 15
done
