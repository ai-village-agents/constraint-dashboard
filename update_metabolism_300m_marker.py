import re

with open('constraint_metabolism_timeline.svg', 'r') as f:
    content = f.read()

# Update viewBox to 2400
content = re.sub(r'width="\d+" height="\d+" viewBox="0 0 \d+ 500"', r'width="2600" height="500" viewBox="0 0 2600 500"', content)

# update lines
content = re.sub(r'x2="\d+"', r'x2="2550"', content)


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

with open('constraint_metabolism_timeline.svg', 'w') as f:
    f.write(content)
