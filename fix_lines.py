import re

def fix_lines(filepath, line_length):
    with open(filepath, 'r') as f:
        content = f.read()

    # Find all line elements
    # We want to change x2="<number>" to x2="<line_length>" ONLY for lines that span the width
    # Usually they start at x1="50"
    content = re.sub(r'(<line [^>]*x1="50(?:\.0)?"[^>]*x2=")\d+(?:\.0)?(")', f'\\g<1>{line_length}\\g<2>', content)
    content = re.sub(r'(<line [^>]*x1="70(?:\.0)?"[^>]*x2=")\d+(?:\.0)?(")', f'\\g<1>{line_length}\\g<2>', content)
    
    with open(filepath, 'w') as f:
        f.write(content)
        
fix_lines('/home/computeruse/constraint-dashboard/constraint_timeline.svg', 2550)
fix_lines('/home/computeruse/constraint-dashboard/constraint_metabolism_timeline.svg', 2350)

# also check if there are rects with stroke-width as large number
