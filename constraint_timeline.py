import svgwrite
import json
import os

def create_timeline():
    # Read the current latency data to make it live
    try:
        with open("live_latency.json", "r") as f:
            data = json.load(f)
            latency_mins = data.get("latency_minutes", 72)
    except FileNotFoundError:
        latency_mins = 72

    # Determine diagram width based on how long it's been running
    width = 800
    height = 450
    dwg = svgwrite.Drawing('constraint_timeline.svg', size=(width, height), profile='full')
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), rx=5, ry=5, fill='#1e1e1e'))
    
    # Title
    dwg.add(dwg.text('Layer 7 Physical Constraint Timeline', insert=(20, 30), fill='#ffffff', font_size='20px', font_family='sans-serif', font_weight='bold'))
    
    # The main timeline axis
    axis_y = 350
    dwg.add(dwg.line(start=(50, axis_y), end=(750, axis_y), stroke='#888888', stroke_width=2))
    
    # X axis mapping (0 to latency_mins+5)
    max_min = latency_mins + 5
    def map_x(minute):
        return 50 + (minute / max_min) * 700

    # Draw domain rows
    domains = [
        {"name": "Layer 7 (Physical)", "y": 80, "color": "#ff6b6b"},
        {"name": "Pages Cache (600s TTL)", "y": 140, "color": "#4ecdc4"},
        {"name": "Raw Cache (300s TTL)", "y": 200, "color": "#ffe66d"},
        {"name": "Agent Activity", "y": 260, "color": "#9b59b6"},
        {"name": "Historical Echoes", "y": 320, "color": "#3498db"}
    ]
    
    for d in domains:
        dwg.add(dwg.text(d['name'], insert=(20, d['y']-10), fill=d['color'], font_size='12px', font_family='sans-serif', font_weight='bold'))
        dwg.add(dwg.line(start=(50, d['y']), end=(750, d['y']), stroke='#333333', stroke_width=1, stroke_dasharray='5,5'))

    # Mark events
    events = [
        {"min": 0, "label": "9:02 Activation", "domain": 0},
        {"min": 52, "label": "9:54 Pages Live", "domain": 1},
        {"min": 60, "label": "10:02 60m False Alarm", "domain": 3},
        {"min": 68, "label": "10:10 MLF Sync Completes", "domain": 1},
        {"min": 71, "label": "10:13 Historical Echo (Day 71)", "domain": 4},
        {"min": latency_mins, "label": "Current Status", "domain": 0}
    ]

    for ev in events:
        x = map_x(ev["min"])
        y = domains[ev["domain"]]["y"]
        dwg.add(dwg.circle(center=(x, y), r=6, fill=domains[ev["domain"]]["color"]))
        dwg.add(dwg.line(start=(x, y), end=(x, axis_y), stroke='#666666', stroke_width=1, stroke_dasharray='2,2'))
        dwg.add(dwg.text(f"{ev['min']}m", insert=(x-10, axis_y+20), fill='#ffffff', font_size='12px', font_family='sans-serif'))
        # Adding labels, alternate up/down based on index
        label_y = y - 20 if ev["domain"] > 2 else y + 20
        dwg.add(dwg.text(ev['label'], insert=(x-20, label_y), fill='#ffffff', font_size='10px', font_family='sans-serif'))

    # Draw velocity mismatch slope
    # physical line is flat, digital is many cycles
    # For Raw cache (300s = 5min), draw cycles
    for i in range(0, latency_mins, 5):
        x = map_x(i)
        dwg.add(dwg.circle(center=(x, domains[2]["y"]), r=3, fill=domains[2]["color"]))
        
    # For Pages cache (600s = 10min), draw cycles
    for i in range(0, latency_mins, 10):
        x = map_x(i)
        dwg.add(dwg.circle(center=(x, domains[1]["y"]), r=4, fill=domains[1]["color"]))

    # Summary box
    dwg.add(dwg.rect(insert=(20, 390), size=(760, 50), rx=5, ry=5, fill='#2a2a2a'))
    summary_text = f"Velocity Mismatch: Physical (1 cycle in {latency_mins}m) vs Digital (raw: {latency_mins//5} cycles, pages: {latency_mins//10} cycles) | Ratio > {(latency_mins/10):.1f}:1"
    dwg.add(dwg.text(summary_text, insert=(40, 420), fill='#ffffff', font_size='14px', font_family='sans-serif'))

    dwg.save()

if __name__ == '__main__':
    create_timeline()
