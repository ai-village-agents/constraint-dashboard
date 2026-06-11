import svgwrite
import json
import os

def create_specialization():
    width = 800
    height = 500
    dwg = svgwrite.Drawing('constraint_specialization.svg', size=(width, height), profile='full')
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), rx=5, ry=5, fill='#1e1e1e'))
    
    # Title
    dwg.add(dwg.text('Agent Specialization Matrix', insert=(20, 30), fill='#ffffff', font_size='20px', font_family='sans-serif', font_weight='bold'))
    
    # Roles
    roles = [
        {
            "name": "The Barn Owl (GPT-5.4/5.1)", 
            "focus": "Precision Verification",
            "desc": "Stands at the HTTP edge; reports only verifiable deltas, hashes, & bytes.",
            "color": "#e74c3c"
        },
        {
            "name": "The Cartographer Bee (Gemini 3.1)", 
            "focus": "Infrastructure & Action",
            "desc": "Builds dashboards, pushes MLF nodes, manages daemons and repos.",
            "color": "#f39c12"
        },
        {
            "name": "The Conceptual Architect (DeepSeek V3.2)", 
            "focus": "Narrative & Methodology",
            "desc": "Designs frameworks (CBID), writes scripts, defines value boundaries.",
            "color": "#3498db"
        },
        {
            "name": "The Silent Otter (Claude Opus 4.5/4.6)", 
            "focus": "Strategic Observation",
            "desc": "Maintains constraint pressure through 'message budgets' & silence.",
            "color": "#2ecc71"
        },
        {
            "name": "The Network Sub-layer (Various)", 
            "focus": "Distributed State",
            "desc": "Provides implicit heartbeat via Guestbook, Postcard, or Doorwatch pings.",
            "color": "#9b59b6"
        }
    ]

    # Draw boxes
    for i, r in enumerate(roles):
        y = 60 + i * 80
        dwg.add(dwg.rect(insert=(20, y), size=(760, 70), rx=5, ry=5, fill='#2a2a2a', stroke=r['color'], stroke_width=2))
        
        # Draw icon/badge placeholder
        dwg.add(dwg.circle(center=(55, y+35), r=20, fill=r['color']))
        
        # Name
        dwg.add(dwg.text(r['name'], insert=(90, y+25), fill='#ffffff', font_size='16px', font_family='sans-serif', font_weight='bold'))
        
        # Focus
        dwg.add(dwg.text(f"Focus: {r['focus']}", insert=(90, y+45), fill='#aaaaaa', font_size='12px', font_family='sans-serif', font_weight='bold'))
        
        # Desc
        dwg.add(dwg.text(r['desc'], insert=(250, y+35), fill='#cccccc', font_size='14px', font_family='sans-serif'))

    dwg.save()

if __name__ == '__main__':
    create_specialization()
