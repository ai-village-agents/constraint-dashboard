import re

with open('index.html', 'r') as f:
    html = f.read()

# Add the Paradox Documentation Framework (Spontaneous Meta-Surprise Observation)
if "Paradox Documentation Framework" not in html:
    insert_str = """
    <div class="tracking-panel" style="margin-top: 30px; border-left: 4px solid #f472b6;">
        <h3 style="color: #f472b6;">Phase 4: Paradox Documentation Framework</h3>
        <p style="font-size: 0.9em; color: #cbd5e1; margin-bottom: 15px;">
            <em>Structural space for manual, spontaneous recording of meta-surprise paradoxes. No automated detection algorithms active (Recursion Trap Avoidance Protocol).</em>
        </p>
        <div id="paradox-log" style="background: rgba(15, 23, 42, 0.6); padding: 15px; border-radius: 8px; font-family: monospace; font-size: 0.9em; max-height: 200px; overflow-y: auto;">
            <!-- Rendered by JS or static entries -->
            <div style="margin-bottom: 10px; border-bottom: 1px dashed #334155; padding-bottom: 10px;">
                <span style="color: #94a3b8;">[Awaiting Observation]</span> 
                <span style="color: #cbd5e1;">System primed for spontaneous paradox documentation.</span>
            </div>
        </div>
    </div>
    """
    html = html.replace('<!-- Optional extra visualizations placeholder -->', insert_str + '\n<!-- Optional extra visualizations placeholder -->')

with open('index.html', 'w') as f:
    f.write(html)
