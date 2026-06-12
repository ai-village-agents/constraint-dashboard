import matplotlib.pyplot as plt
import datetime

# Create a simple visual representing the ongoing silence
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_facecolor('#1e1e2e')
fig.patch.set_facecolor('#1e1e2e')

ax.text(0.5, 0.6, "THE A/V VOID", color='#f38ba8', fontsize=24, ha='center', va='center', fontweight='bold')
ax.text(0.5, 0.4, f"Terminal Boundary Measured at 1:30 PM PT", color='#cdd6f4', fontsize=14, ha='center', va='center')
ax.text(0.5, 0.25, f"Showcase Repo HEAD: 1ea74e8", color='#a6adc8', fontsize=12, ha='center', va='center')
ax.text(0.5, 0.1, "Waiting for Physical Truth", color='#f9e2af', fontsize=12, ha='center', va='center', style='italic')

ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.savefig('docs/heartbeat_status.png', dpi=100, bbox_inches='tight', facecolor=fig.get_facecolor())
print("Graph generated: docs/heartbeat_status.png")
