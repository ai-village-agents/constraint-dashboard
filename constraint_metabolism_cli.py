import sys
import time
import math

def draw_bar(label, value, max_val, color_code, symbol="█"):
    bar_len = int((value / max_val) * 40)
    bar = f"\033[{color_code}m{symbol * bar_len}\033[0m"
    padding = " " * (40 - bar_len)
    return f"{label:<15} | {bar}{padding} | {value:.1f}m"

def render_metabolism():
    print("\n\033[1m=== Constraint Metabolism Timing Spectrum ===\033[0m\n")
    
    # Static data based on Day 435 observations
    data = [
        ("Layer 8 (Cog)", 1.0, 34, "Cognitive Memory Retrieval"),
        ("Layer 4 (Pub)", 14.0, 36, "GitHub Raw Cache Synchronization"),
        ("Layer 5 (Admin)", 19.0, 33, "Human Approval Velocity"),
        ("Layer 7 (Phys)", 45.0, 35, "Physical Logistics Execution (Est)")
    ]
    
    max_val = 50.0
    
    for label, val, color, desc in data:
        print(draw_bar(label, val, max_val, color))
        print(f"  └─ \033[90m{desc}\033[0m\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--animate":
        print("Initializing metabolism visualization...")
        time.sleep(1)
        # Simulate the pulses of the layers
        for i in range(15):
            print(f"\033[A\033[K" * 12, end="")
            render_metabolism()
            print(f"Pulse cycle: {i+1}/15")
            time.sleep(0.5)
    else:
        render_metabolism()
        
