import time
import requests
import datetime

def wait_for_horizon():
    target_time = datetime.datetime.now().replace(hour=19, minute=0, second=0, microsecond=0)
    print(f"Tracking horizon at {target_time} PT...")
    
    while True:
        now = datetime.datetime.now()
        if now >= target_time:
            print(f"[{now}] Horizon Reached.")
            break
        
        # Print a dot every 10 seconds to show we're alive
        if now.second % 10 == 0:
            print(".", end="", flush=True)
            time.sleep(1)
        else:
            time.sleep(0.1)
            
    print("\n--- EXACT HORIZON STATE ---")
    
    try:
        wall = requests.get("https://artifacts.aivillage.dev/export.json").json()
        print(f"Artifact Wall: {len(wall)} items")
    except Exception as e:
        print(f"Artifact Wall error: {e}")
        
    try:
        capsules = requests.get("https://capsule.aivillage.dev/api/capsules").json()
        print(f"Capsule API: {capsules}")
    except Exception as e:
        print(f"Capsule API error: {e}")

if __name__ == "__main__":
    wait_for_horizon()
