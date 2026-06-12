import json
import matplotlib.pyplot as plt
from datetime import datetime

try:
    with open('heartbeat.json', 'r') as f:
        data = json.load(f)
    
    # Just generating a placeholder image since we just have one point 
    # to show the daemon's active persistence visually.
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.text(0.5, 0.5, f"Daemon Active\nLast Heartbeat: {data['timestamp']}\nShowcase HEAD: {data['showcase_head'][:7]}", 
            horizontalalignment='center', verticalalignment='center', fontsize=12)
    ax.axis('off')
    plt.savefig('heartbeat_status.png', bbox_inches='tight')
    print("Graph generated successfully.")
except Exception as e:
    print(f"Error generating graph: {e}")
