import re

file_path = "/home/computeruse/constraint-dashboard/constraint_timeline.svg"

with open(file_path, "r") as f:
    content = f.read()

# Make sure viewBox is exactly 1900 and width is 1900
content = re.sub(r'width="\d+"', 'width="1900"', content, count=1)
content = re.sub(r'viewBox="0 0 \d+ 450"', 'viewBox="0 0 1900 450"', content)

with open(file_path, "w") as f:
    f.write(content)
