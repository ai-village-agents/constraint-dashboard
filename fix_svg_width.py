import re

def update_svg_width(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    # Increase SVG width
    content = re.sub(r'width="800"', 'width="1200" viewBox="0 0 1200 450"', content)
    # Background rect width
    content = re.sub(r'<rect fill="#1e1e1e" height="450" rx="5" ry="5" width="800" x="0" y="0" />',
                     '<rect fill="#1e1e1e" height="450" rx="5" ry="5" width="1200" x="0" y="0" />', content)
    # Bottom rect width
    content = re.sub(r'<rect fill="#2a2a2a" height="50" rx="5" ry="5" width="760" x="20" y="390" />',
                     '<rect fill="#2a2a2a" height="50" rx="5" ry="5" width="1160" x="20" y="390" />', content)
    # Lines
    content = re.sub(r'x2="750"', 'x2="1150"', content)

    with open(filename, 'w') as f:
        f.write(content)

update_svg_width('constraint_timeline.svg')
update_svg_width('constraint_metabolism_timeline.svg')
print("Updated SVG widths to 1200")
