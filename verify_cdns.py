import requests
import time

urls = {
    "raw_svg": "https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/constraint_timeline.svg",
    "pages_svg": "https://ai-village-agents.github.io/constraint-dashboard/constraint_timeline.svg",
    "raw_obs": "https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/docs/OBSERVATION_095.md",
    "pages_obs": "https://ai-village-agents.github.io/constraint-dashboard/docs/OBSERVATION_095.md"
}

for name, url in urls.items():
    try:
        r = requests.get(url, headers={'Cache-Control': 'no-cache'})
        if name.endswith("svg"):
            has_1900 = '1900' in r.text
            print(f"{name}: {r.status_code} | Has 1900px: {has_1900}")
        else:
            print(f"{name}: {r.status_code} | Length: {len(r.text)}")
    except Exception as e:
        print(f"{name}: Error - {e}")
