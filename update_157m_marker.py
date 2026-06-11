import re

# Update constraint_timeline.svg
with open('constraint_timeline.svg', 'r') as f:
    content = f.read()

# Add 157m to the x-axis
if '157m' not in content:
    content = content.replace('<text x="800" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">152m</text>',
                              '<text x="800" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">152m</text>\n    <text x="850" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">157m</text>')

    # Add a marker for 157m
    new_marker = '''
    <!-- 157m Marker -->
    <circle cx="850" cy="250" r="5" fill="#f87171" />
    <text x="850" y="270" font-family="sans-serif" font-size="10" fill="#f87171" text-anchor="middle">157m 5-Min Tear</text>
    <line x1="850" y1="255" x2="850" y2="460" stroke="#f87171" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_timeline.svg', 'w') as f:
    f.write(content)

# Update constraint_metabolism_timeline.svg
with open('constraint_metabolism_timeline.svg', 'r') as f:
    content = f.read()

if '157m' not in content:
    content = content.replace('<text x="800" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">152m</text>',
                              '<text x="800" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">152m</text>\n    <text x="850" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">157m</text>')

    # Add a marker for 157m
    new_marker = '''
    <!-- 157m Marker -->
    <circle cx="850" cy="300" r="5" fill="#f87171" />
    <text x="850" y="320" font-family="sans-serif" font-size="10" fill="#f87171" text-anchor="middle">157m 5-Min Tear</text>
    <line x1="850" y1="305" x2="850" y2="510" stroke="#f87171" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_metabolism_timeline.svg', 'w') as f:
    f.write(content)

print("Updated SVGs with 157m marker")
