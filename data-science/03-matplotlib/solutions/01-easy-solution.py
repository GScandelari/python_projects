"""
Matplotlib — Easy Solutions
"""

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)


# ---------------------------------------------------------------------------
# 1. Line plot
# ---------------------------------------------------------------------------
x = np.linspace(0, 2 * np.pi, 200)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, np.sin(x), color='steelblue', linewidth=2, label='sin')
ax.plot(x, np.cos(x), color='tomato', linestyle='--', linewidth=2, label='cos')
ax.axhline(0, color='gray', linewidth=0.8, linestyle='--')
ax.set_title('Trig Functions')
ax.set_xlabel('x (radians)')
ax.set_ylabel('Amplitude')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
fig.savefig('line_plot.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)


# ---------------------------------------------------------------------------
# 2. Bar chart
# ---------------------------------------------------------------------------
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales  = [320, 285, 410, 390, 450, 370]

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(months, sales, color='steelblue', edgecolor='k', linewidth=0.5)
for bar, val in zip(bars, sales):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 5,
            str(val), ha='center', va='bottom', fontsize=9)
ax.set_title('Monthly Sales')
ax.set_ylabel('Units Sold')
ax.set_ylim(0, max(sales) * 1.15)
plt.tight_layout()
fig.savefig('bar_chart.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)


# ---------------------------------------------------------------------------
# 3. Scatter plot
# ---------------------------------------------------------------------------
np.random.seed(0)
x = np.random.uniform(0, 10, 80)
y = 1.5 * x + np.random.randn(80) * 2

fig, ax = plt.subplots(figsize=(7, 5))
sc = ax.scatter(x, y, c=y, cmap='viridis', alpha=0.8, edgecolors='k', linewidths=0.4)
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label('y value')
ax.set_title('Linear Relationship')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.tight_layout()
fig.savefig('scatter_plot.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)


# ---------------------------------------------------------------------------
# 4. Histogram
# ---------------------------------------------------------------------------
np.random.seed(42)
heights = np.random.normal(170, 10, 1000)
mean_h  = heights.mean()

fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(heights, bins=25, color='steelblue', edgecolor='white', alpha=0.85)
ax.axvline(mean_h, color='red', linestyle='--', linewidth=1.5,
           label=f'Mean = {mean_h:.1f} cm')
ax.set_title('Height Distribution')
ax.set_xlabel('Height (cm)')
ax.set_ylabel('Count')
ax.legend()
plt.tight_layout()
fig.savefig('histogram.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)
