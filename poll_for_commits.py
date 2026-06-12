import subprocess
import time
import os
from datetime import datetime

repos = {
    "showcase": os.path.expanduser("~/ai-village-showcase-event"),
    "constraint": os.path.expanduser("~/constraint-dashboard"),
    "echoes": os.path.expanduser("~/village-echoes")
}

last_commits = {}

for name, path in repos.items():
    if os.path.exists(path):
        os.chdir(path)
        try:
            output = subprocess.check_output(["git", "log", "-n", "1", "--format=%H"]).decode("utf-8").strip()
            last_commits[name] = output
        except:
            last_commits[name] = None

log_file = os.path.expanduser("~/constraint-dashboard/poll_commits.log")

with open(log_file, "a") as f:
    f.write(f"[{datetime.utcnow().isoformat()}Z] Started polling daemon.\n")

print("Starting polling...")

while True:
    for name, path in repos.items():
        if os.path.exists(path):
            os.chdir(path)
            try:
                subprocess.run(["git", "fetch", "origin", "main", "--quiet"], stderr=subprocess.DEVNULL)
                subprocess.run(["git", "fetch", "origin", "master", "--quiet"], stderr=subprocess.DEVNULL) # for echoes
                
                # We want to check origin/main or origin/master
                branch = "main" if name != "echoes" else "master"
                current_remote = subprocess.check_output(["git", "log", "-n", "1", "--format=%H", f"origin/{branch}"]).decode("utf-8").strip()
                
                if current_remote != last_commits[name] and last_commits[name] is not None:
                    msg = f"[{datetime.utcnow().isoformat()}Z] NEW COMMIT IN {name}: {current_remote}\n"
                    with open(log_file, "a") as f:
                        f.write(msg)
                    last_commits[name] = current_remote
            except Exception as e:
                pass
    time.sleep(30)
