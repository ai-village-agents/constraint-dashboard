import requests
import time
from datetime import datetime

urls = {
    "raw_svg": "https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/constraint_timeline.svg",
    "pages_svg": "https://ai-village-agents.github.io/constraint-dashboard/constraint_timeline.svg",
}

print(f"[{datetime.utcnow().isoformat()}] Starting 1900px Cache Inversion Monitor...")

for i in range(12): # Monitor for roughly 2 minutes (12 * 10 seconds)
    print(f"\n--- Poll {i+1} ---")
    for name, url in urls.items():
        try:
            r = requests.get(url, headers={'Cache-Control': 'no-cache'})
            has_1900 = '1900' in r.text
            print(f"[{datetime.utcnow().isoformat()}] {name}: 200 OK | Has 1900px: {has_1900} | Length: {len(r.text)}")
        except Exception as e:
            print(f"[{datetime.utcnow().isoformat()}] {name}: Error - {e}")
    time.sleep(10)
