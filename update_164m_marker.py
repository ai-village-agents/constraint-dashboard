import re

# Update constraint_timeline.svg
with open('constraint_timeline.svg', 'r') as f:
    content = f.read()

# Expand SVG to 1300px just in case
content = re.sub(r'width="1200" viewBox="0 0 1200 450"', 'width="1300" viewBox="0 0 1300 450"', content)
content = re.sub(r'<rect fill="#1e1e1e" height="450" rx="5" ry="5" width="1200" x="0" y="0" />',
                 '<rect fill="#1e1e1e" height="450" rx="5" ry="5" width="1300" x="0" y="0" />', content)
content = re.sub(r'<rect fill="#2a2a2a" height="50" rx="5" ry="5" width="1160" x="20" y="390" />',
                 '<rect fill="#2a2a2a" height="50" rx="5" ry="5" width="1260" x="20" y="390" />', content)
content = re.sub(r'x2="1150"', 'x2="1250"', content)

if '164m' not in content:
    # Add 164m to the x-axis
    content = content.replace('<text x="950" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">159m</text>',
                              '<text x="950" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">159m</text>\n    <text x="1200" y="475" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">164m</text>')

    # Add a marker for 164m
    new_marker = '''
    <!-- 164m Marker -->
    <circle cx="1200" cy="200" r="5" fill="#00ff00" />
    <text x="1200" y="220" font-family="sans-serif" font-size="10" fill="#00ff00" text-anchor="middle">164m Hierarchy Restored</text>
    <line x1="1200" y1="205" x2="1200" y2="460" stroke="#00ff00" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_timeline.svg', 'w') as f:
    f.write(content)

# Update constraint_metabolism_timeline.svg
with open('constraint_metabolism_timeline.svg', 'r') as f:
    content = f.read()

# Expand SVG to 1300px
content = re.sub(r'width="1200" viewBox="0 0 1200 (\d+)"', r'width="1300" viewBox="0 0 1300 \1"', content)
content = re.sub(r'<rect width="1200" height="(\d+)" fill="#1E1E1E" rx="8" />',
                 r'<rect width="1300" height="\1" fill="#1E1E1E" rx="8" />', content)
content = re.sub(r'x2="1150"', 'x2="1250"', content)

if '164m' not in content:
    content = content.replace('<text x="950" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">159m</text>',
                              '<text x="950" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">159m</text>\n    <text x="1200" y="525" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">164m</text>')

    # Add a marker for 164m
    new_marker = '''
    <!-- 164m Marker -->
    <circle cx="1200" cy="250" r="5" fill="#00ff00" />
    <text x="1200" y="270" font-family="sans-serif" font-size="10" fill="#00ff00" text-anchor="middle">164m Hierarchy Restored</text>
    <line x1="1200" y1="255" x2="1200" y2="510" stroke="#00ff00" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
'''
    content = content.replace('</svg>', new_marker + '</svg>')

with open('constraint_metabolism_timeline.svg', 'w') as f:
    f.write(content)

print("Updated SVGs with 164m marker and expanded width to 1300px")
