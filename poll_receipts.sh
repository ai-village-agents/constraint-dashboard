#!/bin/bash
cd ~/constraint-dashboard
while true; do
  git fetch origin
  LOCAL=$(git rev-parse HEAD)
  REMOTE=$(git rev-parse origin/main)
  
  # Only pull if behind, and only run the script periodically anyway
  git pull --rebase origin main >/dev/null 2>&1
  
  python3 update_receipt.py
  
  if git status --porcelain | grep "docs/structural_receipt.html"; then
      git add docs/structural_receipt.html
      git commit -m "auto: update structural receipt from showcase P0 state"
      git push origin main
  fi
  sleep 60
done
