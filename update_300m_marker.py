import re

with open('constraint_timeline.svg', 'r') as f:
    content = f.read()

# Update viewBox to 2400
content = re.sub(r'width="(\d+)" viewBox="0 0 (\d+) 500"', r'width="2600" viewBox="0 0 2600 500"', content)
content = re.sub(r'width="2400" viewBox="0 0 2400 500"', r'width="2600" viewBox="0 0 2600 500"', content)

# update lines and rectangles extending to 2350
content = re.sub(r'x2="2350"', r'x2="2550"', content)
content = re.sub(r'width="2400"', r'width="2600"', content)
content = re.sub(r'stroke-width="2200"', r'stroke-width="2600"', content)

new_marker = """
    <!-- 300m Post-Window Data Drift -->
    <g transform="translate(2100, 0)">
        <line x1="0" y1="50" x2="0" y2="450" stroke="#ffaa00" stroke-width="2" stroke-dasharray="8,4" opacity="0.6"/>
        <circle cx="0" cy="250" r="6" fill="#ffaa00"/>
        <text x="15" y="245" fill="#ffaa00" font-family="monospace" font-size="12" font-weight="bold">300m</text>
        <text x="15" y="260" fill="#a0a0a0" font-family="monospace" font-size="10">5 Hours Waiting</text>
    </g>
</svg>"""

content = content.replace('</svg>', new_marker)

with open('constraint_timeline.svg', 'w') as f:
    f.write(content)
