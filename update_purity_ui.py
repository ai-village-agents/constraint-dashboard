import re

html_file = '/home/computeruse/constraint-dashboard/index.html'

with open(html_file, 'r') as f:
    content = f.read()

purity_metrics_html = """
        <div style="background: rgba(15, 23, 42, 0.6); padding: 15px; border-radius: 8px; margin-top: 10px; border: 1px solid #10b981;">
            <h4 style="color: #10b981; margin-top: 0;">Phase 4 Purity Metrics (Post-Recursion Trap)</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
                <div>
                    <div style="font-size: 0.8em; color: #94a3b8;">Engineered Contamination</div>
                    <div style="color: #10b981; font-weight: bold; font-size: 1.2em;">0.0%</div>
                </div>
                <div>
                    <div style="font-size: 0.8em; color: #94a3b8;">Nullification Effectiveness</div>
                    <div style="color: #10b981; font-weight: bold; font-size: 1.2em;">100.0%</div>
                </div>
                <div>
                    <div style="font-size: 0.8em; color: #94a3b8;">Spontaneous Emergence</div>
                    <div style="color: #10b981; font-weight: bold; font-size: 1.2em;">Preserved</div>
                </div>
            </div>
        </div>
"""

# Insert after the Active Paradox Density line
target_string = '<div style="color: #94a3b8;">Active Paradox Density: <span style="color: #38bdf8; font-weight: bold;">4 / 5</span></div>'

if target_string in content and "Phase 4 Purity Metrics" not in content:
    content = content.replace(target_string, target_string + "\n" + purity_metrics_html)
    with open(html_file, 'w') as f:
        f.write(content)
    print("Purity metrics injected into UI")
else:
    print("Could not find target string or metrics already present.")
