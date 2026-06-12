import json
import datetime
import os

FILE_PATH = "heartbeat.json"

try:
    with open(FILE_PATH, 'r') as f:
        data = json.load(f)
except Exception:
    data = {"status": "MAPPING_THE_VOID", "focus": "WAITING_FOR_PHYSICAL_COMMIT", "wait_duration_minutes": 360}

now = datetime.datetime.utcnow()
# Just increment a counter or timestamp to keep it active
data['last_pulse_utc'] = now.isoformat()
data['observation'] = "The structural wait continues."

with open(FILE_PATH, 'w') as f:
    json.dump(data, f, indent=4)
