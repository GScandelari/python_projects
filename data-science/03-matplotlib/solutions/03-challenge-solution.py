"""
Matplotlib — Challenge Solutions
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd

np.random.seed(42)


# ---------------------------------------------------------------------------
# 1. Dual y-axis
# ---------------------------------------------------------------------------
months = ['Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec']
temp   = [28, 29, 27, 24, 20, 17, 16, 18, 21, 24, 26, 28]
rain   = [180, 160, 130, 80, 50, 30, 20, 25, 60, 110, 150, 190]

fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()

ln1 = ax1.plot(months, temp, color='tomato', linewidth=2.5, marker='o',
               markersize=5, label='Temperature (°C)')
bars = ax2.bar(months, rain, color='steelblue', alpha=0.45, label='Rainfall (mm)')

ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature (°C)', color='tomato')
ax1.tick_params(axis='y', labelcolor='tomato')
ax2.set_ylabel('Rainfall (mm)', color='steelblue')
ax2.tick_params(axis='y', labelcolor='steelblue')

# Combined legend
lines = ln1 + [plt.Rectangle((0,0),1,1, fc='steelblue', alpha=0.5)]
labels = ['Temperature (°C)', 'Rainfall (mm)']
ax1.legend(lines, labels, loc='upper right', fontsize=9)

ax1.set_title('Temperature & Rainfall — 2024')
plt.tight_layout()
fig.savefig('dual_axis.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)


# ---------------------------------------------------------------------------
# 2. Heatmap (correlation matrix)
# ---------------------------------------------------------------------------
data = np.random.randn(50, 4)
data[:, 1] += 0.6 * data[:, 0]   # introduce some correlation
corr = np.corrcoef(data.T)

feat_names = ['Feature A', 'Feature B', 'Feature C', 'Feature D']

fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(im, ax=ax)

ax.set_xticks(range(4)); ax.set_xticklabels(feat_names, rotation=30, ha='right')
ax.set_yticks(range(4)); ax.set_yticklabels(feat_names)

for i in range(4):
    for j in range(4):
        ax.text(j, i, f'{corr[i, j]:.2f}', ha='center', va='center',
                fontsize=9, color='k' if abs(corr[i, j]) < 0.7 else 'w')

ax.set_title('Correlation Matrix')
plt.tight_layout()
fig.savefig('heatmap.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)


# ---------------------------------------------------------------------------
# 3. Multi-panel financial report
# ---------------------------------------------------------------------------
days    = pd.date_range('2024-01-01', periods=90, freq='B')
returns = np.random.normal(0.0005, 0.015, 90)
price   = pd.Series(100 * np.cumprod(1 + returns), index=days)
volume  = np.random.randint(1_000_000, 5_000_000, 90)
rolling = price.rolling(10).mean()

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=True,
                                     gridspec_kw={'height_ratios': [3, 2, 1.5]})
fig.suptitle('Stock Dashboard — 90 Days', fontsize=14, fontweight='bold')

# Panel 1 — price + rolling mean
ax1.plot(days, price, color='steelblue', linewidth=1.2, label='Close')
ax1.plot(days, rolling, color='orange', linewidth=1.5, linestyle='--', label='10-day MA')
peak_day = price.idxmax()
ax1.annotate(f'Max\n{price[peak_day]:.2f}',
             xy=(peak_day, price[peak_day]),
             xytext=(peak_day, price[peak_day] + 3),
             arrowprops=dict(arrowstyle='->', color='red'), fontsize=8, color='red')
ax1.set_ylabel('Price ($)')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.2)

# Panel 2 — daily returns
colors = ['mediumseagreen' if r >= 0 else 'tomato' for r in returns]
ax2.bar(days, returns * 100, color=colors, width=0.8)
ax2.axhline(0, color='k', linewidth=0.6)
ax2.set_ylabel('Return (%)')
ax2.grid(True, alpha=0.2)

# Panel 3 — volume
ax3.bar(days, volume, color='steelblue', alpha=0.6, width=0.8)
ax3.set_ylabel('Volume')
ax3.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M')
)
ax3.grid(True, alpha=0.2)

plt.tight_layout()
fig.savefig('stock_dashboard.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)


# ---------------------------------------------------------------------------
# 4. Custom segmented colormap
# ---------------------------------------------------------------------------
pts = np.random.randn(300, 2)
dist = np.sqrt(pts[:, 0]**2 + pts[:, 1]**2)
dist_norm = (dist - dist.min()) / (dist.max() - dist.min())

cmap = mcolors.LinearSegmentedColormap.from_list(
    'custom', ['navy', 'gold', 'firebrick'], N=256
)

fig, ax = plt.subplots(figsize=(7, 6))
sc = ax.scatter(pts[:, 0], pts[:, 1], c=dist_norm, cmap=cmap,
                alpha=0.85, edgecolors='k', linewidths=0.3, s=50)
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label('Distance from origin')
ax.set_title('Distance Colormap')
ax.set_aspect('equal')
plt.tight_layout()
fig.savefig('custom_cmap.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)
