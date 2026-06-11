import re

# Read SVG
with open('constraint_timeline.svg', 'r') as f:
    svg_data = f.read()

# Update viewBox to fit more data
if 'viewBox="0 0 1800 800"' in svg_data:
    svg_data = svg_data.replace('viewBox="0 0 1800 800"', 'viewBox="0 0 1900 800"')

# Insert the 237m marker
marker = """
    <!-- 237m Showcase Dry-Run Marker -->
    <line x1="1850" y1="200" x2="1850" y2="600" stroke="#ff00ff" stroke-width="2" stroke-dasharray="4,4"/>
    <circle cx="1850" cy="400" r="6" fill="#ff00ff"/>
    <text x="1860" y="380" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">237m Post-Window</text>
    <text x="1860" y="395" fill="#a0a0a0" font-family="sans-serif" font-size="10">Showcase Dry Run</text>
    <text x="1860" y="410" fill="#a0a0a0" font-family="sans-serif" font-size="10">commits verified.</text>
    <text x="1860" y="425" fill="#a0a0a0" font-family="sans-serif" font-size="10">Awaiting Physical Commit.</text>
</svg>"""

svg_data = re.sub(r'</svg>\s*$', marker, svg_data)

# Write it back
with open('constraint_timeline.svg', 'w') as f:
    f.write(svg_data)

print("Added 237m marker to constraint_timeline.svg")
