# Matplotlib

The standard Python library for static, animated, and interactive visualisations.

**Install:** `pip install matplotlib`

**Import convention:** `import matplotlib.pyplot as plt`

---

## 1. Anatomy of a figure

```
Figure
└── Axes (subplot)
    ├── Title
    ├── x-axis (label, ticks, limits)
    ├── y-axis (label, ticks, limits)
    ├── Legend
    └── Plot elements (Line2D, PathCollection, ...)
```

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()   # always use this form — explicit is better
ax.set_title('My Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()
```

## 2. Line plot

```python
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label='sin', color='steelblue', linewidth=2)
ax.plot(x, np.cos(x), label='cos', color='tomato',    linestyle='--')
ax.legend()
ax.set_title('Trig functions')
ax.set_xlabel('x (radians)')
ax.set_ylabel('Amplitude')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## 3. Scatter plot

```python
np.random.seed(0)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

fig, ax = plt.subplots()
ax.scatter(x, y, c='steelblue', alpha=0.6, edgecolors='k', linewidths=0.5)
ax.set_title('Scatter plot')
plt.show()
```

## 4. Bar chart

```python
categories = ['Jan', 'Feb', 'Mar', 'Apr']
values     = [120, 95, 140, 110]

fig, ax = plt.subplots()
bars = ax.bar(categories, values, color='steelblue', edgecolor='k')

# Add value labels on top of each bar
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
            str(val), ha='center', va='bottom', fontsize=9)

ax.set_title('Monthly Sales')
ax.set_ylabel('Units')
plt.show()
```

## 5. Histogram

```python
data = np.random.randn(1000)

fig, ax = plt.subplots()
ax.hist(data, bins=30, color='steelblue', edgecolor='white', alpha=0.8)
ax.set_title('Distribution')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
plt.show()
```

## 6. Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('sin(x)')

axes[0, 1].plot(x, np.cos(x), color='tomato')
axes[0, 1].set_title('cos(x)')

axes[1, 0].scatter(x[:50], np.random.rand(50))
axes[1, 0].set_title('Scatter')

axes[1, 1].hist(np.random.randn(200), bins=20)
axes[1, 1].set_title('Histogram')

fig.suptitle('Overview', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

## 7. Customisation

```python
# Styles
plt.style.use('seaborn-v0_8')    # built-in style
plt.rcParams['figure.figsize'] = (10, 6)  # global default size

# Colours — named, hex, RGB tuple
ax.plot(x, y, color='#2196F3')
ax.plot(x, y, color=(0.1, 0.6, 0.9))

# Markers
ax.plot(x, y, marker='o', markersize=5, markerfacecolor='red')

# Axis limits and ticks
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_xticklabels(['0s', '2s', '4s', '6s', '8s', '10s'])

# Annotations
ax.axhline(y=0, color='k', linewidth=0.8, linestyle='--')  # horizontal line
ax.axvline(x=np.pi, color='gray', linestyle=':')
ax.annotate('Peak', xy=(np.pi/2, 1), xytext=(np.pi/2 + 0.5, 0.8),
            arrowprops=dict(arrowstyle='->'))
```

## 8. Saving figures

```python
fig.savefig('plot.png', dpi=150, bbox_inches='tight')
fig.savefig('plot.svg')          # vector format — scales without blur
fig.savefig('plot.pdf')          # publication quality
plt.close(fig)                   # free memory — important in scripts/loops
```

---

## Quick Reference

```python
fig, ax = plt.subplots(nrows, ncols, figsize=(w, h))
ax.plot(x, y, color=, linestyle=, linewidth=, label=)
ax.scatter(x, y, c=, s=, alpha=, marker=)
ax.bar(x, height, width=, color=, edgecolor=)
ax.hist(x, bins=, color=, edgecolor=, density=)
ax.set_title() / ax.set_xlabel() / ax.set_ylabel()
ax.set_xlim() / ax.set_ylim()
ax.legend() / ax.grid(True, alpha=)
plt.tight_layout()
fig.savefig('file.png', dpi=, bbox_inches='tight')
plt.show() / plt.close(fig)
```

## Practice

| File | Difficulty | Topics |
|---|---|---|
| [01-easy.py](exercises/01-easy.py) | Easy | Line, bar, scatter, histogram |
| [02-medium.py](exercises/02-medium.py) | Medium | Subplots, customisation, annotations |
| [03-challenge.py](exercises/03-challenge.py) | Challenge | Multi-dataset dashboard, secondary axis, heatmap |

Solutions: [solutions/](solutions/)
