import re

def fix_svg(filepath, line_length):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract the viewBox width and height
    match = re.search(r'viewBox="0 0 (\d+) (\d+)"', content)
    if not match:
        print(f"Could not find viewBox in {filepath}")
        return
        
    vb_w, vb_h = match.groups()
    
    # Fix the root svg tag width and height
    content = re.sub(r'width="\d+(px)?"', f'width="{vb_w}"', content, count=1)
    content = re.sub(r'height="\d+(px)?"', f'height="{vb_h}"', content, count=1)

    # Fix the root rect tag
    content = re.sub(r'<rect fill="#(?:1e1e1e|1E1E1E)" height="\d+(?:%)?" rx="\d+" ry="\d+" width="\d+(?:%)?"', 
                     f'<rect fill="#1e1e1e" height="{vb_h}" rx="5" ry="5" width="{vb_w}"', content, count=1)

    # Note: metabolism already uses 100% for the background rect, which is better.
    if 'metabolism' in filepath:
        content = re.sub(r'<rect fill="#(?:1e1e1e|1E1E1E)" height="100%" width="100%"', 
                         f'<rect fill="#1e1e1e" height="100%" width="100%"', content, count=1)
        
    # Fix the standard timeline lines length
    # Specifically looking for stroke-width attributes that are acting as length
    content = re.sub(r'stroke-width="\d+" x1="50(?:\.0)?" x2="\d+(?:\.0)?"', f'stroke-width="1" x1="50" x2="{line_length}"', content)
    content = re.sub(r'stroke-width="\d+" x1="70" x2="\d+"', f'stroke-width="1" x1="70" x2="{line_length}"', content)
    
    # The current lines use stroke-width as the length which is very wrong (it makes them super thick lines).
    # Wait, SVG lines use x1, y1, x2, y2. The script was changing stroke-width to the length, which is bizarre.
    # Let's fix that.
    content = re.sub(r'stroke-width="\d+" (x1="[^"]+" x2="\d+")', r'stroke-width="1" \1', content)
    content = re.sub(r'x2="\d+"( y1="\d+" y2="\d+")', f'x2="{line_length}"\\1', content)

    # specific fix for the inner rect on the main timeline
    if 'timeline' in filepath and 'metabolism' not in filepath:
        inner_rect_width = int(vb_w) - 40
        content = re.sub(r'<rect fill="#2a2a2a" height="50" rx="5" ry="5" width="\d+"', 
                         f'<rect fill="#2a2a2a" height="50" rx="5" ry="5" width="{inner_rect_width}"', content)

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Fixed {filepath}")

# constraint_timeline is viewBox 2600 500, line length should be 2550
fix_svg('/home/computeruse/constraint-dashboard/constraint_timeline.svg', 2550)
# constraint_metabolism_timeline is viewBox 2400 500, line length should be 2350
fix_svg('/home/computeruse/constraint-dashboard/constraint_metabolism_timeline.svg', 2350)
