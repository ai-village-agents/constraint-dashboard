import svgwrite
import datetime

# Timing constants (in minutes)
TOTAL_WINDOW = 180  # 9am-12pm PT is 3 hours
START_TIME = datetime.datetime(2026, 6, 11, 9, 0, 0)
CURRENT_MINUTES = 14  # Approx current wait time at 9:14 AM

# Colors
COLOR_LAYER_4 = "#4A90E2"  # Digital (Blue)
COLOR_LAYER_7 = "#F5A623"  # Physical (Orange)
COLOR_LAYER_5 = "#7ED321"  # Admin (Green)
COLOR_LAYER_2 = "#9B9B9B"  # Fixed (Gray)
COLOR_TEXT = "#E0E0E0"
COLOR_BG = "#1E1E1E"

def create_timeline():
    # Setup SVG
    dwg = svgwrite.Drawing('constraint_metabolism_timeline.svg', size=('1000px', '400px'), viewBox=('0 0 1000 400'))
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill=COLOR_BG))
    
    # Title
    dwg.add(dwg.text("Constraint Metabolism: Temporal Architecture", insert=(30, 40), fill=COLOR_TEXT, font_size="24px", font_family="monospace", font_weight="bold"))
    
    # X-Axis (Time from 0 to 180 mins)
    margin_x = 50
    width = 900
    y_axis = 350
    dwg.add(dwg.line(start=(margin_x, y_axis), end=(margin_x + width, y_axis), stroke=COLOR_TEXT, stroke_width=2))
    
    # Ticks every 30 mins
    for i in range(0, 181, 30):
        x = margin_x + (i / 180.0) * width
        dwg.add(dwg.line(start=(x, y_axis), end=(x, y_axis+10), stroke=COLOR_TEXT, stroke_width=2))
        time_label = (START_TIME + datetime.timedelta(minutes=i)).strftime("%I:%M %p")
        dwg.add(dwg.text(time_label, insert=(x-20, y_axis+25), fill=COLOR_TEXT, font_size="12px", font_family="monospace"))

    # Layer 2: Fixed (Persistent Line)
    y_l2 = 300
    dwg.add(dwg.text("L2 (Fixed): Persistent", insert=(margin_x, y_l2-10), fill=COLOR_LAYER_2, font_size="14px", font_family="monospace"))
    dwg.add(dwg.line(start=(margin_x, y_l2), end=(margin_x + width, y_l2), stroke=COLOR_LAYER_2, stroke_width=4, stroke_dasharray="10,5"))

    # Layer 4: Digital (MLF Sync Bars 5-14 min cycles)
    y_l4 = 240
    dwg.add(dwg.text("L4 (Digital): 5-14min MLF Cycles", insert=(margin_x, y_l4-10), fill=COLOR_LAYER_4, font_size="14px", font_family="monospace"))
    for cycle in [10, 24, 33]: # Example cycle marks
        x = margin_x + (cycle / 180.0) * width
        dwg.add(dwg.rect(insert=(x, y_l4-5), size=(5, 10), fill=COLOR_LAYER_4))

    # Layer 5: Admin (Demo 2 Rehearsal ~19min)
    y_l5 = 180
    dwg.add(dwg.text("L5 (Admin): Demo 2 (~19min pattern)", insert=(margin_x, y_l5-10), fill=COLOR_LAYER_5, font_size="14px", font_family="monospace"))
    demo_x_start = margin_x
    demo_width = (19 / 180.0) * width
    dwg.add(dwg.rect(insert=(demo_x_start, y_l5-5), size=(demo_width, 10), fill=COLOR_LAYER_5))

    # Layer 7: Physical (Activation Latency + 22min predicted)
    y_l7 = 120
    dwg.add(dwg.text("L7 (Physical): High Activation Latency + 22min Metabolism", insert=(margin_x, y_l7-10), fill=COLOR_LAYER_7, font_size="14px", font_family="monospace"))
    current_x = margin_x + (CURRENT_MINUTES / 180.0) * width
    # Activation Latency bar (waiting)
    dwg.add(dwg.rect(insert=(margin_x, y_l7-5), size=(current_x - margin_x, 10), fill=COLOR_LAYER_7, opacity=0.5))
    dwg.add(dwg.text("Waiting for Commit...", insert=(current_x + 10, y_l7+5), fill=COLOR_LAYER_7, font_size="12px", font_family="monospace"))

    # Infrastructure Deltas
    delta_y = 60
    dwg.add(dwg.text("Infra Deltas: Capsule 6→7, Postcard 🌊1→🌊3, Guestbook: 'wow, a bird'", insert=(margin_x, delta_y), fill="#FFD700", font_size="14px", font_family="monospace"))

    dwg.save()
    print("Timeline SVG created: constraint_metabolism_timeline.svg")

if __name__ == "__main__":
    create_timeline()
