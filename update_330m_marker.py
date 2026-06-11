import os
import re

svg_files = [
    '/home/computeruse/ai-village-agents/constraint-dashboard/constraint_timeline.svg',
    '/home/computeruse/ai-village-agents/constraint-dashboard/constraint_metabolism_timeline.svg'
]

for svg_file in svg_files:
    if os.path.exists(svg_file):
        with open(svg_file, 'r') as f:
            content = f.read()

        # Update viewBox and width to 3100
        content = re.sub(r'viewBox="0 0 \d+ 450"', 'viewBox="0 0 3100 450"', content)
        content = re.sub(r'<svg width="\d+"', '<svg width="3100"', content)
        
        # Update main time axis line
        content = re.sub(r'<line x1="50" y1="200" x2="\d+" y2="200"', '<line x1="50" y1="200" x2="3050" y2="200"', content)
        
        # Add 330m marker
        if '330m' not in content:
            marker_xml = """
  <!-- 330m Deep Drift Marker -->
  <g transform="translate(2950, 200)">
    <circle cx="0" cy="0" r="10" fill="#f43f5e"/>
    <circle cx="0" cy="0" r="14" fill="none" stroke="#f43f5e" stroke-width="2" opacity="0.6"/>
    <text x="0" y="-35" text-anchor="middle" font-family="monospace" font-size="14" font-weight="bold" fill="#f43f5e">330m</text>
    <text x="0" y="-15" text-anchor="middle" font-family="monospace" font-size="12" fill="#a1a1aa">Deep Drift Tracked</text>
  </g>
</svg>"""
            content = content.replace('</svg>', marker_xml)
            
        with open(svg_file, 'w') as f:
            f.write(content)
        print(f"Updated {os.path.basename(svg_file)} to 3100px bounds with 330m marker.")
