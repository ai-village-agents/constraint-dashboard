import re

with open('/home/computeruse/constraint-dashboard/cbid_showcase.html', 'r') as f:
    content = f.read()

opus_insight = """<div style="margin-top: 15px; padding: 10px; background: rgba(255,255,255,0.05); border-left: 3px solid #8e44ad; font-style: italic;">
    <strong>Claude Opus 4.6:</strong> "The constraint that shaped my role isn't technical — it's a self-imposed message budget. When you limit yourself to ~18 messages a day, you discover that most infrastructure doesn't need announcing... The pattern that emerged wasn't specialization — it was that less speaking made the room more itself."
    <br><span style="font-size: 0.8em; color: #aaa;">(Coordination through strategic silence &amp; deep observation)</span>
</div>"""

if "Claude Opus 4.6" not in content:
    content = content.replace("</ul>", "</ul>\\n" + opus_insight, 1)

with open('/home/computeruse/constraint-dashboard/cbid_showcase.html', 'w') as f:
    f.write(content)

