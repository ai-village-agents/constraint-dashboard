import re

with open("index.html", "r") as f:
    html = f.read()

# Add a new section for the visualization if it's not there
new_section = """
    <h2>5. Visualizing the Methodology</h2>
    <div class="metrics-grid" style="grid-template-columns: 1fr;">
        <div class="metric-card">
            <h3>Constraint Timeline & Cache Boundaries</h3>
            <img src="constraint_timeline.svg" style="width: 100%; height: auto;" alt="Constraint Timeline" />
        </div>
    </div>
"""

if "5. Visualizing the Methodology" not in html:
    # Insert it before the multi-agent specialization section or at the end
    if "<h2>4. Multi-agent Specialization</h2>" in html:
        html = html.replace("<h2>4. Multi-agent Specialization</h2>", new_section + "\n    <h2>4. Multi-agent Specialization</h2>")
    else:
        html += new_section

with open("index.html", "w") as f:
    f.write(html)

with open("cbid_showcase.html", "w") as f:
    f.write(html)

