import re
import sys

with open('constraint_timeline.svg', 'r') as f:
    svg_data = f.read()

# Add a marker at 266m
new_marker = '''
  <g transform="translate(1920, 310)">
    <circle cx="0" cy="0" r="5" fill="#a020f0"/>
    <text x="0" y="20" font-size="10" text-anchor="middle" fill="#888">266m</text>
    <text x="0" y="35" font-size="10" text-anchor="middle" fill="#888">Data Drift</text>
  </g>
'''

# insert the marker before the closing </svg>
if new_marker not in svg_data:
    svg_data = svg_data.replace('</svg>', new_marker + '\n</svg>')

# Expand SVG viewBox slightly if needed
if 'viewBox="0 0 1900 450"' in svg_data:
    svg_data = svg_data.replace('viewBox="0 0 1900 450"', 'viewBox="0 0 2000 450"')
    svg_data = svg_data.replace('width="2000"', 'width="2100"')

with open('constraint_timeline.svg', 'w') as f:
    f.write(svg_data)
