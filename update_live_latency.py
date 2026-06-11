import json
import time
from datetime import datetime, timezone
import os

# The start of the physical latency window
# Note: June 11 is daylight saving time (PDT), so UTC-7
start_timestamp = datetime(2026, 6, 11, 16, 0, 0, tzinfo=timezone.utc).timestamp()

def update_latency_json():
    current_timestamp = time.time()
    
    # Calculate difference in minutes
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
    
    # Also check if a logistics commit has actually happened by reading the monitor log
    monitor_log_path = os.path.expanduser("~/showcase_monitor.log")
    try:
        with open(monitor_log_path, 'r') as f:
            log_content = f.read()
            # Fixed the check to require Costco or FedEx to prevent false positives from generic "logistics" mentions
            if "costco" in log_content.lower() or "fedex" in log_content.lower():
                 data["status"] = "PHYSICAL_CONSTRAINT_RESOLVED"
                 data["trigger"] = "Logistics commit detected!"
    except FileNotFoundError:
        pass

    with open("/home/computeruse/constraint-dashboard/live_latency.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    update_latency_json()
