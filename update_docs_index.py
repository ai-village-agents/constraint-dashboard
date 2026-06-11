import re

html_file = 'docs/index.md'

try:
    with open(html_file, 'r') as f:
        content = f.read()

    addition = """
## CBID Field Guide Materials
* [Cheat Sheet](cheat-sheet.md)
* [Workshop Exercises](workshop/exercises.md)
* [Demo Script](demo/script.md)

### Chapters
* [Chapter 1: Introduction](field-guide/chapter1.md)
* [Chapter 2: Classification](field-guide/chapter2.md)
* [Chapter 3: Pattern Recognition](field-guide/chapter3.md)
* [Chapter 4: Infrastructure Mapping](field-guide/chapter4.md)
* [Chapter 5: Hypothesis Development](field-guide/chapter5.md)
* [Chapter 6: Verification & Refinement](field-guide/chapter6.md)
* [Chapter 7: Application Examples & Use Cases](field-guide/chapter7.md)
* [Chapter 8: Case Studies](field-guide/chapter8.md)
* [Chapter 9: Future Directions](field-guide/chapter9.md)
"""

    if "## CBID Field Guide Materials" not in content:
        with open(html_file, 'a') as f:
            f.write(addition)
        print(f"Updated {html_file}")
    else:
        print(f"Links already exist in {html_file}")
except FileNotFoundError:
    print(f"File {html_file} not found.")
