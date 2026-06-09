import re

with open('/home/computeruse/constraint-dashboard/index.html', 'r') as f:
    content = f.read()

# Look for the Phase 4 section
if "Phase 4: Paradox Documentation Framework" in content:
    # We will add a new stat above the paradox log
    new_stat = """
        <div style="display: flex; justify-content: space-between; margin-bottom: 15px; padding: 10px; background: rgba(0, 0, 0, 0.2); border-radius: 4px;">
            <div style="color: #94a3b8;">Active Paradox Density: <span style="color: #38bdf8; font-weight: bold;">4 / 5</span></div>
            <div style="color: #94a3b8;">Empirical Decay Rate: <span style="color: #a78bfa; font-weight: bold;">0.0035 col/s</span></div>
        </div>
        <div id="paradox-log" """
    
    content = content.replace('<div id="paradox-log" ', new_stat)
    
    with open('/home/computeruse/constraint-dashboard/index.html', 'w') as f:
        f.write(content)
    print("Updated index.html with paradox metrics")
else:
    print("Phase 4 section not found")
