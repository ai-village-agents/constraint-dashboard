import re

# Update constraint_timeline.svg
with open('constraint_timeline.svg', 'r') as f:
    content = f.read()

# Add 148m to the x-axis
if '148m' not in content:
    content = content.replace('<text x="700" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">138m</text>',
                              '<text x="700" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">138m</text>\n    <text x="750" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">148m</text>')

    # Add a marker for 148m
    new_marker = '''
    <!-- 148m Marker -->
    <circle cx="750" cy="300" r="5" fill="#f472b6" />
    <text x="750" y="320" font-family="sans-serif" font-size="10" fill="#f472b6" text-anchor="middle">148m Inversion Split</text>
    <line x1="750" y1="305" x2="750" y2="460" stroke="#f472b6" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_timeline.svg', 'w') as f:
    f.write(content)

# Update constraint_metabolism_timeline.svg
with open('constraint_metabolism_timeline.svg', 'r') as f:
    content = f.read()

if '148m' not in content:
    content = content.replace('<text x="700" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">138m</text>',
                              '<text x="700" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">138m</text>\n    <text x="750" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">148m</text>')

    # Add a marker for 148m
    new_marker = '''
    <!-- 148m Marker -->
    <circle cx="750" cy="350" r="5" fill="#f472b6" />
    <text x="750" y="370" font-family="sans-serif" font-size="10" fill="#f472b6" text-anchor="middle">148m Inversion Split</text>
    <line x1="750" y1="355" x2="750" y2="510" stroke="#f472b6" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_metabolism_timeline.svg', 'w') as f:
    f.write(content)

print("Updated SVGs with 148m marker")
