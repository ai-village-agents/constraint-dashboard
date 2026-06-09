import re

html_file = '/home/computeruse/constraint-dashboard/index.html'

with open(html_file, 'r') as f:
    content = f.read()

purity_metrics_html = """
                <div class="metric-card">
                    <h4>Phase 4 Purity Metrics</h4>
                    <p>Engineered Expectation Contamination: <span id="engineered-expectation" class="highlight">0.0%</span></p>
                    <p>Observation Nullification Effectiveness: <span id="observation-nullification" class="highlight">100.0%</span></p>
                    <p>Spontaneous Emergence Preservation: <span id="spontaneous-preservation" class="highlight">Active (Post-Mod 4 Nullification)</span></p>
                </div>
"""

# Insert the purity metrics card after the stability paradox card
if "stability-paradox-card" in content and "engineered-expectation" not in content:
    parts = content.split('<div id="stability-paradox-card"')
    new_content = parts[0] + purity_metrics_html + '<div id="stability-paradox-card"' + parts[1]
    
    with open(html_file, 'w') as f:
        f.write(new_content)
    print("Purity metrics added to index.html")
else:
    print("UI update skipped: Target insertion point not found or metrics already present.")

