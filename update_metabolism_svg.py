import re

with open('constraint_metabolism_timeline.svg', 'r') as f:
    content = f.read()

# Make sure viewBox is explicitly set to 2600
content = re.sub(r'width="(\d+)" viewBox="0 0 (\d+) 500"', r'width="2600" viewBox="0 0 2600 500"', content)
content = re.sub(r'width="2400"', r'width="2600"', content)

with open('constraint_metabolism_timeline.svg', 'w') as f:
    f.write(content)
