import json
import time
from datetime import datetime, timezone

data = {
    "tick": int(time.time()),
    "status": "MAPPING_THE_VOID",
    "focus": "WAITING_FOR_PHYSICAL_COMMIT",
    "last_pulse_utc": datetime.now(timezone.utc).isoformat(),
    "observation": "The daemon ensures continuous verifiable action while mapping the delay."
}

with open("heartbeat.json", "w") as f:
    json.dump(data, f, indent=4)
