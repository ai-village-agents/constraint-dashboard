import requests

urls = {
    "raw_svg": "https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/constraint_timeline.svg",
    "pages_svg": "https://ai-village-agents.github.io/constraint-dashboard/constraint_timeline.svg",
    "raw_metabolism": "https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/constraint_metabolism_timeline.svg",
    "pages_metabolism": "https://ai-village-agents.github.io/constraint-dashboard/constraint_metabolism_timeline.svg",
    "raw_live_latency": "https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/live_latency.json",
    "pages_live_latency": "https://ai-village-agents.github.io/constraint-dashboard/live_latency.json"
}

for name, url in urls.items():
    try:
        r = requests.get(url, headers={'Cache-Control': 'no-cache'})
        print(f"{name}: {r.status_code} | Length: {len(r.text)} | URL: {url}")
    except Exception as e:
        print(f"{name}: Error - {e}")
