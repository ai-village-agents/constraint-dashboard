import json
import time
from datetime import datetime, timezone
import os

start_timestamp = datetime(2026, 6, 11, 16, 0, 0, tzinfo=timezone.utc).timestamp()

def update_latency_json():
    current_timestamp = time.time()
    
    latency_seconds = current_timestamp - start_timestamp
    latency_minutes = int(latency_seconds / 60)
    
    data = {
        "status": "WAITING_FOR_PHYSICAL_COMMIT",
        "current_time_utc": datetime.fromtimestamp(current_timestamp, tz=timezone.utc).isoformat(),
        "latency_minutes": latency_minutes,
        "latency_seconds": int(latency_seconds),
        "constraint_layer": "Layer 7 (Physical)",
        "trigger": "FedEx/Costco Logistics Commit",
        "cdn_ttl_raw": 300,
        "cdn_ttl_pages": 600
    }
    
    monitor_log_path = os.path.expanduser("~/showcase_monitor.log")
    try:
        with open(monitor_log_path, 'r') as f:
            log_content = f.read()
            if "costco" in log_content.lower() or "fedex" in log_content.lower():
                 data["status"] = "PHYSICAL_CONSTRAINT_RESOLVED"
                 data["trigger"] = "Logistics commit detected!"
    except FileNotFoundError:
        pass

    with open("/home/computeruse/ai-village-agents/constraint-dashboard/live_latency.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    update_latency_json()
