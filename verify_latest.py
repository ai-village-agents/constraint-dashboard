import urllib.request
import json
import time

def check_endpoint(url):
    try:
        req = urllib.request.Request(url, headers={'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        return {"error": str(e)}

timestamp = int(time.time())
pages_url = f"https://ai-village-agents.github.io/constraint-dashboard/live_latency.json?cb={timestamp}"
raw_url = f"https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/live_latency.json?cb={timestamp}"

pages_data = check_endpoint(pages_url)
raw_data = check_endpoint(raw_url)

print(f"Pages Status: {pages_data.get('status')} | Min: {pages_data.get('latency_minutes')}")
print(f"Raw Status: {raw_data.get('status')} | Min: {raw_data.get('latency_minutes')}")
