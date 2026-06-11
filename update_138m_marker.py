import re

# Update constraint_timeline.svg
with open('constraint_timeline.svg', 'r') as f:
    content = f.read()

# Add 138m to the x-axis
if '138m' not in content:
    # Find the position of 110m and add 138m
    content = content.replace('<text x="640" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">110m</text>',
                              '<text x="640" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">110m</text>\n    <text x="700" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">138m</text>')

    # Add a marker for 138m
    new_marker = '''
    <!-- 138m Marker -->
    <circle cx="700" cy="300" r="5" fill="#4ade80" />
    <text x="700" y="320" font-family="sans-serif" font-size="10" fill="#4ade80" text-anchor="middle">138m structural tear</text>
    <line x1="700" y1="305" x2="700" y2="460" stroke="#4ade80" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_timeline.svg', 'w') as f:
    f.write(content)

# Update constraint_metabolism_timeline.svg
with open('constraint_metabolism_timeline.svg', 'r') as f:
    content = f.read()

if '138m' not in content:
    # Find the position of 110m and add 138m
    content = content.replace('<text x="640" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">110m</text>',
                              '<text x="640" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">110m</text>\n    <text x="700" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">138m</text>')

    # Add a marker for 138m
    new_marker = '''
    <!-- 138m Marker -->
    <circle cx="700" cy="350" r="5" fill="#4ade80" />
    <text x="700" y="370" font-family="sans-serif" font-size="10" fill="#4ade80" text-anchor="middle">138m structural tear</text>
    <line x1="700" y1="355" x2="700" y2="510" stroke="#4ade80" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_metabolism_timeline.svg', 'w') as f:
    f.write(content)

print("Updated SVGs with 138m marker")
