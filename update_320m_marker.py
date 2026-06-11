import re

def expand_svg(filepath, marker_x, marker_label, marker_time, marker_color):
    with open(filepath, 'r') as f:
        content = f.read()

    # Expand the bounds explicitly to 3000px width
    new_width = "3000"
    content = content.replace('viewBox="0 0 2600 500"', f'viewBox="0 0 {new_width} 500"')
    content = content.replace('width="2600"', f'width="{new_width}"')
    
    content = content.replace('x2="2550"', f'x2="2950"')
    
    # Specific fix for the text rects
    content = content.replace('width="2560" x="20"', 'width="2960" x="20"')
    
    # Inject the actual 320m marker
    if "320m" not in content and marker_label == "320m":
        marker = f'''<circle cx="{marker_x}" cy="80" fill="{marker_color}" r="6" /><line stroke="#666666" stroke-dasharray="2,2" stroke-width="1" x1="{marker_x}" x2="{marker_x}" y1="80" y2="350" /><text fill="#ffffff" font-family="sans-serif" font-size="12px" x="{marker_x - 10}" y="370">{marker_label}</text><text fill="#ffffff" font-family="sans-serif" font-size="10px" x="{marker_x - 20}" y="100">{marker_time}</text>'''
        insert_idx = content.rfind('<rect fill="#2a2a2a"')
        if insert_idx != -1:
            content = content[:insert_idx] + marker + "\n" + content[insert_idx:]

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Expanded and added marker to {filepath}")

# 320m marker calculation:
# scale is 8.75px per minute.
# 320m = 50 + (320 * 8.75) = 2850
expand_svg('/home/computeruse/constraint-dashboard/constraint_timeline.svg', 2850.0, "320m", "14:20 320m Deep Drift", "#ff6b6b")

# Also metabolism timeline which scales differently maybe? No, let's just update bounds.
def expand_metabolism(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    new_width = "3000"
    content = content.replace('viewBox="0 0 2600 500"', f'viewBox="0 0 {new_width} 500"')
    content = content.replace('width="2600"', f'width="{new_width}"')
    content = content.replace('x2="2550"', f'x2="2950"')
    
    with open(filepath, 'w') as f:
        f.write(content)

expand_metabolism('/home/computeruse/constraint-dashboard/constraint_metabolism_timeline.svg')
