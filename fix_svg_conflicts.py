import re

def fix_conflict(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Find the conflict block
    conflict_pattern = r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> [a-f0-9]+ \(.*?\)'
    match = re.search(conflict_pattern, content, re.DOTALL)
    
    if match:
        head_content = match.group(1)
        new_content = match.group(2)
        
        # Combine both contents
        resolved_content = content[:match.start()] + head_content + "\n" + new_content + content[match.end():]
        
        with open(filename, 'w') as f:
            f.write(resolved_content)
        print(f"Fixed {filename}")
    else:
        print(f"No conflict found in {filename}")

fix_conflict('~/constraint-dashboard/constraint_timeline.svg'.replace('~', '/home/computeruse'))
fix_conflict('~/constraint-dashboard/constraint_metabolism_timeline.svg'.replace('~', '/home/computeruse'))
