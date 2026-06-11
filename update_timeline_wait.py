import re

with open('metabolism_timeline_viz.py', 'r') as f:
    content = f.read()

# Update the CURRENT_MINUTES constant
content = re.sub(r'CURRENT_MINUTES = \d+', 'CURRENT_MINUTES = 28', content)
content = re.sub(r'Activation Waiting \(\>25m\)', 'Activation Waiting (>28m)', content)

with open('metabolism_timeline_viz.py', 'w') as f:
    f.write(content)

print("Updated timeline script with CURRENT_MINUTES = 28.")
