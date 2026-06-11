import re

def update_svg(filename, marker_x, label, fill_color, base_y):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if label not in content:
        # We find the last text x anchor, maybe 164m
        # Let's just insert it before </svg> for safety, this is easier
        new_marker = f'''
    <!-- {label} Marker -->
    <circle cx="{marker_x}" cy="{base_y}" r="5" fill="{fill_color}" />
    <text x="{marker_x}" y="{base_y + 20}" font-family="sans-serif" font-size="10" fill="{fill_color}" text-anchor="middle">{label}</text>
    <line x1="{marker_x}" y1="{base_y + 5}" x2="{marker_x}" y2="{base_y + 260}" stroke="{fill_color}" stroke-width="1" stroke-dasharray="2,2" opacity="0.3" />
    <text x="{marker_x}" y="{base_y + 275}" font-family="sans-serif" font-size="12" fill="#aaa" text-anchor="middle">168m</text>
'''
        content = content.replace('</svg>', new_marker + '\n</svg>')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename} with {label}")

update_svg('constraint_timeline.svg', 1250, '168m End of Window Approach', '#00ffff', 200)
update_svg('constraint_metabolism_timeline.svg', 1250, '168m End of Window Approach', '#00ffff', 250)
