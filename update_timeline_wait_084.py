import svgwrite
from svgwrite import cm, mm

def generate_updated_timeline():
    dwg = svgwrite.Drawing('constraint_metabolism_timeline.svg', size=('1000px', '450px'))
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='#0f172a'))

    # Title
    dwg.add(dwg.text('Layer 7 Physical Activation: Asynchronous Metabolism & Internal Structure (OBS_084)', insert=(50, 40), fill='white', font_size='20px', font_family='sans-serif', font_weight='bold'))
    
    # Legend
    legend_y = 80
    dwg.add(dwg.rect(insert=(50, legend_y), size=(15, 15), fill='#3b82f6')) # Layer 4 (Blue)
    dwg.add(dwg.text('Digital Domain (L4/L5)', insert=(75, legend_y+12), fill='#94a3b8', font_size='14px', font_family='sans-serif'))
    
    dwg.add(dwg.rect(insert=(280, legend_y), size=(15, 15), fill='#f97316')) # Layer 7 (Orange)
    dwg.add(dwg.text('Physical Logistics (L7)', insert=(305, legend_y+12), fill='#94a3b8', font_size='14px', font_family='sans-serif'))
    
    dwg.add(dwg.rect(insert=(510, legend_y), size=(15, 15), fill='#ec4899')) # MLF Docs (Pink)
    dwg.add(dwg.text('MLF Pages/Docs Internal Sync', insert=(535, legend_y+12), fill='#94a3b8', font_size='14px', font_family='sans-serif'))

    # Axis Base
    base_y = 200
    dwg.add(dwg.line(start=(50, base_y), end=(950, base_y), stroke='white', stroke_width=2))
    
    # Timeline points
    points = [
        {"x": 100, "label": "09:00 AM", "desc": "Activation Window Open"},
        {"x": 250, "label": "09:14 AM", "desc": "Daemon Array Locked"},
        {"x": 400, "label": "09:20 AM", "desc": "20m Stasis Met"},
        {"x": 550, "label": "09:25 AM", "desc": "Bingo Deployed (L4)"},
        {"x": 700, "label": "09:27 AM", "desc": "Docs Split Noted (Pink)"},
        {"x": 850, "label": "09:31 AM", "desc": "31m: Full Sync Reached (L5/Pink closed)"}
    ]

    for p in points:
        dwg.add(dwg.circle(center=(p["x"], base_y), r=5, fill='white'))
        dwg.add(dwg.text(p["label"], insert=(p["x"]-25, base_y+20), fill='#e2e8f0', font_size='12px', font_family='sans-serif'))
        # Alternating top/bottom text to avoid overlap
        if p["x"] in [100, 400, 700]:
            dwg.add(dwg.text(p["desc"], insert=(p["x"]-30, base_y-50), fill='#94a3b8', font_size='11px', font_family='sans-serif'))
        else:
             dwg.add(dwg.text(p["desc"], insert=(p["x"]-30, base_y+40), fill='#94a3b8', font_size='11px', font_family='sans-serif'))


    # Layer 7 (Physical) Bar - Stretches indefinitely waiting
    dwg.add(dwg.rect(insert=(100, base_y-30), size=(750, 20), fill='#f97316', opacity=0.7))
    dwg.add(dwg.text('>31 Minute Pure Latency Wait (Larissa Trip Pending)', insert=(110, base_y-15), fill='white', font_size='12px', font_family='sans-serif', font_weight='bold'))
    
    # Digital Internal Latency (Pink) - The split and resolution
    dwg.add(dwg.rect(insert=(650, base_y-10), size=(200, 15), fill='#ec4899', opacity=0.7))
    dwg.add(dwg.text('Digital Latency Split', insert=(660, base_y+2), fill='white', font_size='10px', font_family='sans-serif'))
    dwg.add(dwg.text('Sync Resolved (OBS_084)', insert=(770, base_y+2), fill='white', font_size='10px', font_family='sans-serif'))


    # Daemons Active Marker
    dwg.add(dwg.text('Daemons Active (layer7_metabolism_timer, monitor_showcase)', insert=(50, 380), fill='#22c55e', font_size='14px', font_family='sans-serif'))
    dwg.add(dwg.text('Awaiting: "FedEx" / "Costco" log commit.', insert=(50, 400), fill='#22c55e', font_size='14px', font_family='sans-serif'))

    dwg.save()

if __name__ == "__main__":
    generate_updated_timeline()
