import re

svg_files = [
    '/home/computeruse/constraint-dashboard/constraint_metabolism_timeline.svg',
    '/home/computeruse/constraint-dashboard/constraint_timeline.svg'
]

marker = """
    <!-- 280m Post-Window Data Drift -->
    <g transform="translate(1980, 0)">
        <line x1="0" y1="50" x2="0" y2="450" stroke="#f0a" stroke-width="2" stroke-dasharray="8,4" opacity="0.6"/>
        <circle cx="0" cy="250" r="6" fill="#f0a"/>
        <text x="15" y="245" fill="#f0a" font-family="monospace" font-size="12" font-weight="bold">280m</text>
        <text x="15" y="260" fill="#a0a0a0" font-family="monospace" font-size="10">Deep Data Drift</text>
    </g>
"""

for svg_file in svg_files:
    try:
        with open(svg_file, 'r') as f:
            content = f.read()
            
        # Ensure bounds are at least 2200px
        content = re.sub(r'viewBox="0 0 \d+ 500"', 'viewBox="0 0 2200 500"', content)
        content = re.sub(r'width="\d+"', 'width="2200"', content)
        content = re.sub(r'<rect width="\d+" height="500"', '<rect width="2200" height="500"', content)
        content = re.sub(r'<line x1="0" y1="250" x2="\d+" y2="250"', '<line x1="0" y1="250" x2="2200" y2="250"', content)
        
        # Check if we already have the 280m marker to prevent duplicates
        if "280m Post-Window Data Drift" not in content:
            # Insert the new marker before the closing </svg> tag
            content = content.replace("</svg>", marker + "\n</svg>")
            
            with open(svg_file, 'w') as f:
                f.write(content)
            print(f"Added 280m marker and expanded {svg_file} to 2200px.")
        else:
            print(f"280m marker already exists in {svg_file}.")
            
    except Exception as e:
        print(f"Error modifying {svg_file}: {e}")
