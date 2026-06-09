import re

with open('index.html', 'r') as f:
    html = f.read()

# Add a section to display autonomous modifications if it doesn't exist
if "Autonomous Modifications Log" not in html:
    insert_str = """
    <div class="tracking-panel" style="margin-top: 30px;">
        <h3 style="color: #fbbf24;">Autonomous Modifications Log</h3>
        <div id="modifications-list" style="background: rgba(15, 23, 42, 0.6); padding: 15px; border-radius: 8px; font-family: monospace; font-size: 0.9em; max-height: 200px; overflow-y: auto;">
            <!-- Rendered by JS -->
        </div>
    </div>
    """
    html = html.replace('<!-- Optional extra visualizations placeholder -->', insert_str + '\n<!-- Optional extra visualizations placeholder -->')

# Update the JS to render modifications
js_patch = """
                    // Render modifications
                    const modsList = document.getElementById('modifications-list');
                    if (modsList && val.autonomous_modifications) {
                        modsList.innerHTML = val.autonomous_modifications.map(mod => `
                            <div style="margin-bottom: 10px; border-bottom: 1px solid #334155; padding-bottom: 10px;">
                                <span style="color: #94a3b8;">[${mod.timestamp.split('T')[1].split('.')[0]}]</span> 
                                <span style="color: #38bdf8;">${mod.target_constraint}</span>: 
                                <span style="color: #ef4444;">${mod.previous_intensity}</span> &rarr; <span style="color: #4ade80;">${mod.new_intensity}</span>
                                <br><span style="color: #cbd5e1; font-size: 0.9em;">Parameters: &alpha;=${mod.engine_parameters_used.alpha}, &beta;=${mod.engine_parameters_used.beta}, &gamma;=${mod.engine_parameters_used.gamma}</span>
                            </div>
                        `).join('');
                    }
"""

if "const modsList =" not in html:
    html = html.replace("const chartHtml = `", js_patch + "\nconst chartHtml = `")

with open('index.html', 'w') as f:
    f.write(html)
