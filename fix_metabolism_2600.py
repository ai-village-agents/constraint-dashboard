with open('/home/computeruse/constraint-dashboard/constraint_metabolism_timeline.svg', 'r') as f:
    content = f.read()

content = content.replace('viewBox="0 0 2400 500"', 'viewBox="0 0 2600 500"')
content = content.replace('width="2400"', 'width="2600"')
content = content.replace('x2="2350"', 'x2="2550"')

with open('/home/computeruse/constraint-dashboard/constraint_metabolism_timeline.svg', 'w') as f:
    f.write(content)
