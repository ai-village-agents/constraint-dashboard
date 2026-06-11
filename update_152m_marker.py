import re

# Update constraint_timeline.svg
with open('constraint_timeline.svg', 'r') as f:
    content = f.read()

# Add 152m to the x-axis
if '152m' not in content:
    content = content.replace('<text x="750" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">148m</text>',
                              '<text x="750" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">148m</text>\n    <text x="800" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">152m</text>')

    # Add a marker for 152m
    new_marker = '''
    <!-- 152m Marker -->
    <circle cx="800" cy="300" r="5" fill="#facc15" />
    <text x="800" y="320" font-family="sans-serif" font-size="10" fill="#facc15" text-anchor="middle">152m Cache Re-Split</text>
    <line x1="800" y1="305" x2="800" y2="460" stroke="#facc15" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_timeline.svg', 'w') as f:
    f.write(content)

# Update constraint_metabolism_timeline.svg
with open('constraint_metabolism_timeline.svg', 'r') as f:
    content = f.read()

if '152m' not in content:
    content = content.replace('<text x="750" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">148m</text>',
                              '<text x="750" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">148m</text>\n    <text x="800" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">152m</text>')

    # Add a marker for 152m
    new_marker = '''
    <!-- 152m Marker -->
    <circle cx="800" cy="350" r="5" fill="#facc15" />
    <text x="800" y="370" font-family="sans-serif" font-size="10" fill="#facc15" text-anchor="middle">152m Cache Re-Split</text>
    <line x1="800" y1="355" x2="800" y2="510" stroke="#facc15" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_metabolism_timeline.svg', 'w') as f:
    f.write(content)

print("Updated SVGs with 152m marker")
