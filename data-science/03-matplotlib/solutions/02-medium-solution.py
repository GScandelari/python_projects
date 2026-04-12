"""
Matplotlib — Medium Solutions
"""

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ---------------------------------------------------------------------------
# 1. 2×2 subplot grid
# ---------------------------------------------------------------------------
x   = np.linspace(0, 2 * np.pi, 200)
products  = ['A', 'B', 'C', 'D', 'E']
prod_sales = [450, 310, 520, 280, 390]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# [0,0] Line
axes[0, 0].plot(x, np.sin(x), label='sin(x)')
axes[0, 0].plot(x, np.sin(2 * x), label='sin(2x)', linestyle='--')
axes[0, 0].legend()
axes[0, 0].set_title('sin(x) and sin(2x)')

# [0,1] Bar
axes[0, 1].bar(products, prod_sales, color='steelblue', edgecolor='k')
axes[0, 1].set_title('Product Sales')
axes[0, 1].set_ylabel('Units')

# [1,0] Scatter
px = np.random.randn(50)
py = np.random.randn(50)
pz = np.sqrt(px**2 + py**2)
axes[1, 0].scatter(px, py, c=pz, cmap='plasma', alpha=0.8)
axes[1, 0].set_title('Scatter — coloured by distance')

# [1,1] Histogram
axes[1, 1].hist(np.random.exponential(scale=2, size=500), bins=25,
                color='tomato', edgecolor='white')
axes[1, 1].set_title('Exponential distribution')

fig.suptitle('Data Dashboard', fontsize=14, fontweight='bold')
plt.tight_layout()
fig.savefig('2x2_dashboard.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)


# ---------------------------------------------------------------------------
# 2. Stacked bar chart
# ---------------------------------------------------------------------------
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
north = [120, 135, 128, 150]
south = [ 95, 110, 105, 118]
east  = [ 80,  90,  88, 102]

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(quarters, north, label='North', color='steelblue')
ax.bar(quarters, south, bottom=north, label='South', color='tomato')
bottom_ns = [n + s for n, s in zip(north, south)]
ax.bar(quarters, east, bottom=bottom_ns, label='East', color='mediumseagreen')
ax.set_title('Quarterly Revenue by Region')
ax.set_ylabel('Revenue (R$k)')
ax.legend()
plt.tight_layout()
fig.savefig('stacked_bar.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)


# ---------------------------------------------------------------------------
# 3. Annotations and reference lines
# ---------------------------------------------------------------------------
np.random.seed(1)
t    = np.linspace(0, 4 * np.pi, 200)
sig  = 2 * np.sin(t) + np.random.randn(200) * 0.3
mean = sig.mean()
std  = sig.std()

peak_idx = np.argmax(sig)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t, sig, color='steelblue', linewidth=1.2, label='Signal')
ax.axhline(mean, color='gray', linestyle='--', linewidth=1, label=f'Mean = {mean:.2f}')
ax.fill_between(t, mean - std, mean + std, alpha=0.15, color='orange', label='Mean ± 1 std')
ax.annotate('Peak', xy=(t[peak_idx], sig[peak_idx]),
            xytext=(t[peak_idx] + 0.5, sig[peak_idx] - 0.5),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=9, color='red')
ax.set_title('Signal with Annotations')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.2)
plt.tight_layout()
fig.savefig('annotated_signal.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)


# ---------------------------------------------------------------------------
# 4. Horizontal bar chart — ranked
# ---------------------------------------------------------------------------
languages = ['Python','Java','C','C++','JavaScript','Go','Rust','Kotlin']
scores    = [100, 74, 72, 65, 63, 42, 38, 34]

# Sort ascending so the highest ends up at the top
sorted_pairs = sorted(zip(scores, languages))
scores_s, langs_s = zip(*sorted_pairs)

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(langs_s, scores_s, color='steelblue', edgecolor='k', linewidth=0.5)
for bar, val in zip(bars, scores_s):
    ax.text(val + 1, bar.get_y() + bar.get_height() / 2,
            str(val), va='center', fontsize=9)
ax.set_title('Language Popularity Index')
ax.set_xlabel('Score')
ax.set_xlim(0, 115)
plt.tight_layout()
fig.savefig('hbar_ranked.png', dpi=120, bbox_inches='tight')
plt.show()
plt.close(fig)
