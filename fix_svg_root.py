import re

svg_files = [
    '/home/computeruse/constraint-dashboard/constraint_metabolism_timeline.svg',
    '/home/computeruse/constraint-dashboard/constraint_timeline.svg'
]

for svg_file in svg_files:
    try:
        with open(svg_file, 'r') as f:
            content = f.read()
            
        # The viewBox attribute in the root <svg> tag is currently "0 0 2000 450" 
        # but the width is 2200. This is what GPT-5.4 noticed.
        # We need to explicitly match the root tag and update its viewBox to match the width.
        # We will also ensure it's not cutting off anything at the right edge by setting width to 2400.
        
        # Replace the <svg ...> tag specifically
        svg_pattern = r'<svg[^>]+>'
        match = re.search(svg_pattern, content)
        if match:
            svg_tag = match.group(0)
            
            # Replace width and viewBox in the svg tag
            new_svg_tag = re.sub(r'width="\d+"', 'width="2400"', svg_tag)
            new_svg_tag = re.sub(r'viewBox="[^"]+"', 'viewBox="0 0 2400 500"', new_svg_tag)
            
            content = content.replace(svg_tag, new_svg_tag)
            
        # Also fix the background rect which has a second viewBox inside it
        rect_pattern = r'<rect fill="#1e1e1e" height="450" rx="5" ry="5"[^>]+>'
        match = re.search(rect_pattern, content)
        if match:
            rect_tag = match.group(0)
            new_rect_tag = re.sub(r'width="\d+"', 'width="2400"', rect_tag)
            # Remove viewBox from rect if it exists (it shouldn't be on a rect)
            new_rect_tag = re.sub(r' viewBox="[^"]+"', '', new_rect_tag)
            
            content = content.replace(rect_tag, new_rect_tag)
            
        # Ensure the main timeline lines stretch to the end
        content = re.sub(r'x2="\d+"( y1="350")', 'x2="2350"\\1', content)
        content = re.sub(r'x2="\d+"( y1="80")', 'x2="2350"\\1', content)
        content = re.sub(r'x2="\d+"( y1="140")', 'x2="2350"\\1', content)
        content = re.sub(r'x2="\d+"( y1="200")', 'x2="2350"\\1', content)
        content = re.sub(r'x2="\d+"( y1="260")', 'x2="2350"\\1', content)
        content = re.sub(r'x2="\d+"( y1="320")', 'x2="2350"\\1', content)

        with open(svg_file, 'w') as f:
            f.write(content)
        print(f"Fixed {svg_file} root viewBox and expanded to 2400px.")
    except Exception as e:
        print(f"Error modifying {svg_file}: {e}")
