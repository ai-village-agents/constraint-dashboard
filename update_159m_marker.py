import re

# Update constraint_timeline.svg
with open('constraint_timeline.svg', 'r') as f:
    content = f.read()

# Add 159m to the x-axis
if '159m' not in content:
    content = content.replace('<text x="900" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">158m</text>',
                              '<text x="900" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">158m</text>\n    <text x="950" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">159m</text>')

    # Add a marker for 159m
    new_marker = '''
    <!-- 159m Marker -->
    <circle cx="950" cy="200" r="5" fill="#fuchsia" />
    <text x="950" y="220" font-family="sans-serif" font-size="10" fill="#fuchsia" text-anchor="middle">159m Major Inversion</text>
    <line x1="950" y1="205" x2="950" y2="460" stroke="#fuchsia" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_timeline.svg', 'w') as f:
    f.write(content)

# Update constraint_metabolism_timeline.svg
with open('constraint_metabolism_timeline.svg', 'r') as f:
    content = f.read()

if '159m' not in content:
    content = content.replace('<text x="900" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">158m</text>',
                              '<text x="900" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">158m</text>\n    <text x="950" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">159m</text>')

    # Add a marker for 159m
    new_marker = '''
    <!-- 159m Marker -->
    <circle cx="950" cy="250" r="5" fill="#fuchsia" />
    <text x="950" y="270" font-family="sans-serif" font-size="10" fill="#fuchsia" text-anchor="middle">159m Major Inversion</text>
    <line x1="950" y1="255" x2="950" y2="510" stroke="#fuchsia" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_metabolism_timeline.svg', 'w') as f:
    f.write(content)

print("Updated SVGs with 159m marker")
