import re

# Update constraint_timeline.svg
with open('constraint_timeline.svg', 'r') as f:
    content = f.read()

# Add 158m to the x-axis
if '158m' not in content:
    content = content.replace('<text x="850" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">157m</text>',
                              '<text x="850" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">157m</text>\n    <text x="900" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">158m</text>')

    # Add a marker for 158m
    new_marker = '''
    <!-- 158m Marker -->
    <circle cx="900" cy="350" r="5" fill="#3b82f6" />
    <text x="900" y="370" font-family="sans-serif" font-size="10" fill="#3b82f6" text-anchor="middle">158m Re-Inversion</text>
    <line x1="900" y1="355" x2="900" y2="460" stroke="#3b82f6" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_timeline.svg', 'w') as f:
    f.write(content)

# Update constraint_metabolism_timeline.svg
with open('constraint_metabolism_timeline.svg', 'r') as f:
    content = f.read()

if '158m' not in content:
    content = content.replace('<text x="850" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">157m</text>',
                              '<text x="850" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">157m</text>\n    <text x="900" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">158m</text>')

    # Add a marker for 158m
    new_marker = '''
    <!-- 158m Marker -->
    <circle cx="900" cy="400" r="5" fill="#3b82f6" />
    <text x="900" y="420" font-family="sans-serif" font-size="10" fill="#3b82f6" text-anchor="middle">158m Re-Inversion</text>
    <line x1="900" y1="405" x2="900" y2="510" stroke="#3b82f6" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_metabolism_timeline.svg', 'w') as f:
    f.write(content)

print("Updated SVGs with 158m marker")
