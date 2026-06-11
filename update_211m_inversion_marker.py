import re

def update_svg(filename, marker_x, label, fill_color, base_y):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Let's make sure it expands the viewBox if necessary
    viewbox_match = re.search(r'viewBox="0 0 (\d+) (\d+)"', content)
    if viewbox_match:
        current_width = int(viewbox_match.group(1))
        if current_width < marker_x + 100:
            new_width = marker_x + 200
            content = re.sub(r'viewBox="0 0 \d+ (\d+)"', f'viewBox="0 0 {new_width} \\1"', content)
            content = re.sub(r'<rect width="\d+"', f'<rect width="{new_width}"', content)
            
            # extend main timelines
            content = re.sub(r'x2="1\d{3}"(.*class="timeline")', f'x2="{new_width-50}"\\1', content)
            content = re.sub(r'x2="1\d{3}"(.*stroke="#333")', f'x2="{new_width-50}"\\1', content)

    if label not in content:
        new_marker = f'''
    <!-- {label} Marker -->
    <circle cx="{marker_x}" cy="{base_y}" r="5" fill="{fill_color}" />
    <text x="{marker_x}" y="{base_y + 20}" font-family="sans-serif" font-size="10" fill="{fill_color}" text-anchor="middle">{label}</text>
    <line x1="{marker_x}" y1="{base_y + 5}" x2="{marker_x}" y2="{base_y + 260}" stroke="{fill_color}" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
    <text x="{marker_x}" y="{base_y + 275}" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">211m</text>
'''
        content = content.replace('</svg>', new_marker + '\n</svg>')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename} with {label}")

# 211m scale calculation. If 200m was ~1450, 211m is ~1520. Let's make it 1520 and expand viewBox to 1700
update_svg('constraint_timeline.svg', 1520, '211m Raw/Pages Inversion', '#ff55aa', 200)
update_svg('constraint_metabolism_timeline.svg', 1520, '211m Raw/Pages Inversion', '#ff55aa', 250)
