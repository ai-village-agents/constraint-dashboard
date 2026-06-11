import svgwrite
import datetime

# Timing constants (in minutes)
TOTAL_WINDOW = 180  # 9am-12pm PT is 3 hours
START_TIME = datetime.datetime(2026, 6, 11, 9, 0, 0)
CURRENT_MINUTES = 28  # Updated wait time

# Colors
COLOR_LAYER_4 = "#4A90E2"  # Digital (Blue)
COLOR_LAYER_7 = "#F5A623"  # Physical (Orange)
COLOR_LAYER_5 = "#7ED321"  # Admin (Green)
COLOR_LAYER_2 = "#9B9B9B"  # Fixed (Gray)
COLOR_MLF_INTERNAL = "#FF69B4" # Hot Pink for MLF Internal Sync
COLOR_TEXT = "#E0E0E0"
COLOR_BG = "#1E1E1E"

def create_timeline():
    # Setup SVG
    dwg = svgwrite.Drawing('constraint_metabolism_timeline.svg', size=('1000px', '500px'), viewBox=('0 0 1000 500'))
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill=COLOR_BG))
    
    # Title
    dwg.add(dwg.text("Constraint Metabolism: Temporal Architecture & MLF Internal Sync", insert=(30, 40), fill=COLOR_TEXT, font_size="22px", font_family="monospace", font_weight="bold"))
    
    # X-Axis (Time from 0 to 180 mins)
    margin_x = 50
    width = 900
    y_axis = 450
    dwg.add(dwg.line(start=(margin_x, y_axis), end=(margin_x + width, y_axis), stroke=COLOR_TEXT, stroke_width=2))
    
    # Ticks every 30 mins
    for i in range(0, 181, 30):
        x = margin_x + (i / 180.0) * width
        dwg.add(dwg.line(start=(x, y_axis), end=(x, y_axis+10), stroke=COLOR_TEXT, stroke_width=2))
        time_label = (START_TIME + datetime.timedelta(minutes=i)).strftime("%I:%M %p")
        dwg.add(dwg.text(time_label, insert=(x-20, y_axis+25), fill=COLOR_TEXT, font_size="12px", font_family="monospace"))

    # Layer 2: Fixed (Persistent Line)
    y_l2 = 400
    dwg.add(dwg.text("L2 (Fixed): Persistent", insert=(margin_x, y_l2-10), fill=COLOR_LAYER_2, font_size="14px", font_family="monospace"))
    dwg.add(dwg.line(start=(margin_x, y_l2), end=(margin_x + width, y_l2), stroke=COLOR_LAYER_2, stroke_width=4, stroke_dasharray="10,5"))

    # Layer 4: Digital (MLF Sync Bars 5-14 min cycles)
    y_l4 = 340
    dwg.add(dwg.text("L4 (Digital): Overall 5-14min cycles", insert=(margin_x, y_l4-10), fill=COLOR_LAYER_4, font_size="14px", font_family="monospace"))
    for cycle in [10, 24, 33]: # Example cycle marks
        x = margin_x + (cycle / 180.0) * width
        dwg.add(dwg.rect(insert=(x, y_l4-5), size=(5, 10), fill=COLOR_LAYER_4))

    # MLF INTERNAL SYNC (Sub-layer of L4)
    y_mlf = 280
    dwg.add(dwg.text("MLF Internal Temporal Structure: ~15min Sync Cycle", insert=(margin_x, y_mlf-15), fill=COLOR_MLF_INTERNAL, font_size="14px", font_family="monospace", font_weight="bold"))
    
    # Draw internal sync phases
    sync_start_x = margin_x + (15 / 180.0) * width
    sync_mid_x = margin_x + (22 / 180.0) * width
    sync_end_x = margin_x + (30 / 180.0) * width
    
    # 1. Registry (Fast)
    dwg.add(dwg.circle(center=(sync_start_x, y_mlf), r=4, fill=COLOR_MLF_INTERNAL))
    dwg.add(dwg.text("1. Registry (Immediate)", insert=(sync_start_x - 10, y_mlf+15), fill=COLOR_TEXT, font_size="10px", font_family="monospace"))
    
    # 2. HEAD Pointer (Medium)
    dwg.add(dwg.line(start=(sync_start_x, y_mlf), end=(sync_mid_x, y_mlf), stroke=COLOR_MLF_INTERNAL, stroke_width=2))
    dwg.add(dwg.circle(center=(sync_mid_x, y_mlf), r=4, fill=COLOR_MLF_INTERNAL))
    dwg.add(dwg.text("2. HEAD Array Split (~7m)", insert=(sync_mid_x - 30, y_mlf-10), fill=COLOR_TEXT, font_size="10px", font_family="monospace"))
    
    # 3. Docs (Slow)
    dwg.add(dwg.line(start=(sync_mid_x, y_mlf), end=(sync_end_x, y_mlf), stroke=COLOR_MLF_INTERNAL, stroke_width=2, stroke_dasharray="4,2"))
    dwg.add(dwg.circle(center=(sync_end_x, y_mlf), r=4, fill=COLOR_MLF_INTERNAL))
    dwg.add(dwg.text("3. Docs Synced (~15m total)", insert=(sync_end_x - 10, y_mlf+15), fill=COLOR_TEXT, font_size="10px", font_family="monospace"))


    # Layer 5: Admin (Demo 2 Rehearsal ~19min)
    y_l5 = 200
    dwg.add(dwg.text("L5 (Admin): Demo 2 (~19min rehearsal pattern)", insert=(margin_x, y_l5-10), fill=COLOR_LAYER_5, font_size="14px", font_family="monospace"))
    demo_x_start = margin_x
    demo_width = (19 / 180.0) * width
    dwg.add(dwg.rect(insert=(demo_x_start, y_l5-5), size=(demo_width, 10), fill=COLOR_LAYER_5))

    # Layer 7: Physical (Activation Latency + 22min predicted)
    y_l7 = 140
    dwg.add(dwg.text("L7 (Physical): High Activation Latency + 22min Metabolism", insert=(margin_x, y_l7-10), fill=COLOR_LAYER_7, font_size="14px", font_family="monospace"))
    current_x = margin_x + (CURRENT_MINUTES / 180.0) * width
    # Activation Latency bar (waiting)
    dwg.add(dwg.rect(insert=(margin_x, y_l7-5), size=(current_x - margin_x, 10), fill=COLOR_LAYER_7, opacity=0.5))
    dwg.add(dwg.text("Activation Waiting (>28m)...", insert=(current_x + 10, y_l7+5), fill=COLOR_LAYER_7, font_size="12px", font_family="monospace"))

    # Infrastructure Deltas
    delta_y = 80
    dwg.add(dwg.text("Infra Asynchronous State: MLF (325 nodes), Showcase (33 cards), Guestbook (10: 'wow, a bird')", insert=(margin_x, delta_y), fill="#FFD700", font_size="14px", font_family="monospace"))

    dwg.save()
    print("Timeline SVG created: constraint_metabolism_timeline.svg")

if __name__ == "__main__":
    create_timeline()
