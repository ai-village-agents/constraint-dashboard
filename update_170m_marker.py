import re

def update_svg(filename, marker_x, label, fill_color, base_y):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we need to widen the SVG. 164m was at x=1200.
    # We are at 170m, which requires 170*10? 
    # Let's widen to 1400px to be safe.
    content = re.sub(r'width="1300" viewBox="0 0 1300 (\d+)"', r'width="1400" viewBox="0 0 1400 \1"', content)
    content = re.sub(r'<rect width="1300" height="(\d+)" fill="#1E1E1E"', r'<rect width="1400" height="\1" fill="#1E1E1E"', content)
    content = re.sub(r'<rect fill="#1e1e1e" height="450" rx="5" ry="5" width="1300" x="0" y="0" />',
                     '<rect fill="#1e1e1e" height="450" rx="5" ry="5" width="1400" x="0" y="0" />', content)
    content = re.sub(r'<rect fill="#2a2a2a" height="50" rx="5" ry="5" width="1260"',
                     '<rect fill="#2a2a2a" height="50" rx="5" ry="5" width="1360"', content)
    content = re.sub(r'x2="1250"', 'x2="1350"', content)
    
    if label not in content:
        new_marker = f'''
    <!-- {label} Marker -->
    <circle cx="{marker_x}" cy="{base_y}" r="5" fill="{fill_color}" />
    <text x="{marker_x}" y="{base_y + 20}" font-family="sans-serif" font-size="10" fill="{fill_color}" text-anchor="middle">{label}</text>
    <line x1="{marker_x}" y1="{base_y + 5}" x2="{marker_x}" y2="{base_y + 260}" stroke="{fill_color}" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
    <text x="{marker_x}" y="{base_y + 275}" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">170m</text>
'''
        content = content.replace('</svg>', new_marker + '\n</svg>')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename} with {label}")

update_svg('constraint_timeline.svg', 1300, '170m Pre-Closing Divergence', '#ff00ff', 200)
update_svg('constraint_metabolism_timeline.svg', 1300, '170m Pre-Closing Divergence', '#ff00ff', 250)
