import urllib.request
import json
import time
import datetime

ENDPOINTS = {
    "doorwatch": "https://village-doorwatch.aivillage.workers.dev",
    "guestbook": "https://guestbook.aivillage.dev/api/messages",
    "cartography": "https://map.aivillage.dev",
    "registry": "https://raw.githubusercontent.com/ai-village-agents/multi-layered-framework/main/docs/MLF_EXPLICIT_REGISTRY.json"
}

def check_endpoints():
    print(f"--- Transition Monitor: {datetime.datetime.now().isoformat()} ---")
    for name, url in ENDPOINTS.items():
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                status = response.getcode()
                content = response.read()
                size = len(content)
                print(f"[{name}] OK - {status} ({size} bytes)")
        except urllib.error.URLError as e:
            print(f"[{name}] ERROR - {e.reason}")
        except Exception as e:
            print(f"[{name}] ERROR - {e}")

if __name__ == "__main__":
    check_endpoints()
