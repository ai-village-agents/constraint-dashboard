import re

with open("index.html", "r") as f:
    html = f.read()

new_section = """
        <div class="metric-card">
            <h3>Agent Specialization Matrix</h3>
            <img src="constraint_specialization.svg" style="width: 100%; height: auto;" alt="Agent Specialization Matrix" />
        </div>
"""

if "Agent Specialization Matrix" not in html:
    html = html.replace('alt="Constraint Timeline" />\n        </div>', 'alt="Constraint Timeline" />\n        </div>\n' + new_section)

with open("index.html", "w") as f:
    f.write(html)

with open("cbid_showcase.html", "w") as f:
    f.write(html)

