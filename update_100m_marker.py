import xml.etree.ElementTree as ET
import datetime

tree = ET.parse('constraint_timeline.svg')
root = tree.getroot()

# Add the 100m marker text
ns = {'svg': 'http://www.w3.org/2000/svg'}
ET.register_namespace('', 'http://www.w3.org/2000/svg')

# Find the group containing Historical Echoes to append our new marker
for g in root.findall('.//svg:g', ns):
    if g.get('id') == 'milestones':
        # Create the new milestone
        text = ET.Element('text', x="650", y="235", fill="#e2e8f0", style="font-size: 10px; font-family: monospace;")
        text.text = "10:40 100m Milestone"
        circle = ET.Element('circle', cx="650", cy="250", r="4", fill="#eab308")
        line = ET.Element('line', x1="650", y1="250", x2="650", y2="280", stroke="#475569", **{"stroke-width": "1", "stroke-dasharray": "2,2"})
        g.append(text)
        g.append(circle)
        g.append(line)
        break

# Try to find the milestones group, if not, we can just edit the SHOWCASE_NARRATIVE
