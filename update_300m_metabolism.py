import re

with open('constraint_metabolism_timeline.svg', 'r') as f:
    content = f.read()

# Update viewBox
content = re.sub(r'width="(\d+)" viewBox="0 0 (\d+) 500"', r'width="2600" viewBox="0 0 2600 500"', content)
content = re.sub(r'width="2400" viewBox="0 0 2400 500"', r'width="2600" viewBox="0 0 2600 500"', content)

# update lines and rectangles
content = re.sub(r'x2="2350"', r'x2="2550"', content)

with open('constraint_metabolism_timeline.svg', 'w') as f:
    f.write(content)
