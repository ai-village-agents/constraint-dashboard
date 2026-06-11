import urllib.request
import time

urls = {
    "Raw": "https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/live_latency.json",
    "Pages": "https://ai-village-agents.github.io/constraint-dashboard/live_latency.json"
}

for name, url in urls.items():
    req = urllib.request.Request(url)
    req.add_header('Cache-Control', 'no-cache')
    try:
        response = urllib.request.urlopen(req)
        content = response.read().decode('utf-8')
        headers = dict(response.headers)
        import json
        try:
            data = json.loads(content)
            print(f"{name}: latency_minutes={data.get('latency_minutes')} | status={data.get('status')} | Cache-Control={headers.get('cache-control')}")
        except json.JSONDecodeError:
            print(f"{name}: Failed to parse JSON")
    except Exception as e:
        print(f"{name} Error: {e}")
