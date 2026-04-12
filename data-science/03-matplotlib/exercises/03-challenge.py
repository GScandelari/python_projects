"""
Matplotlib — Challenge Exercises
==================================
Topics: secondary axis, heatmap, multi-panel report, custom colourmap,
        animated plot, event-driven annotation.

Run:  python 03-challenge.py
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd

np.random.seed(42)


# ---------------------------------------------------------------------------
# 1. Dual y-axis (secondary axis)
# ---------------------------------------------------------------------------
# Plot monthly temperature (°C) as a line on the left y-axis
# and monthly rainfall (mm) as bars on the right y-axis.
# Requirements:
# - Use ax.twinx() for the secondary axis
# - Different colours for each series; add a combined legend
# - Title: 'Temperature & Rainfall — 2024'
# - x-label: 'Month'
# Save as 'dual_axis.png'

months = ['Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec']
temp   = [28, 29, 27, 24, 20, 17, 16, 18, 21, 24, 26, 28]
rain   = [180, 160, 130, 80, 50, 30, 20, 25, 60, 110, 150, 190]

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Heatmap (correlation matrix)
# ---------------------------------------------------------------------------
# Generate a 50×4 random dataset (4 features).
# Compute the Pearson correlation matrix with numpy.
# Requirements:
# - Display as a heatmap using ax.imshow with the 'coolwarm' colormap
# - Set vmin=-1, vmax=1
# - Add a colorbar
# - Annotate each cell with the rounded correlation value (2 decimal places)
# - Tick labels: ['Feature A', 'Feature B', 'Feature C', 'Feature D']
# - Title: 'Correlation Matrix'
# Save as 'heatmap.png'

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Multi-panel financial report
# ---------------------------------------------------------------------------
# Build a 3-row figure (figsize 10×12) using GridSpec or subplots,
# showing a 90-day simulated stock:
#
# Panel 1 (top, large): closing price line + 10-day rolling mean
# Panel 2 (middle):     daily returns (bar chart, positive=green, negative=red)
# Panel 3 (bottom):     volume bars (random integers 1M–5M)
#
# Requirements:
# - All panels share the x-axis (sharex=True)
# - Panel 1: annotate the global maximum with an arrow
# - Title above the whole figure: 'Stock Dashboard — 90 Days'
# Save as 'stock_dashboard.png'

days    = pd.date_range('2024-01-01', periods=90, freq='B')
returns = np.random.normal(0.0005, 0.015, 90)
price   = pd.Series(100 * np.cumprod(1 + returns), index=days)
volume  = np.random.randint(1_000_000, 5_000_000, 90)

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Custom segmented colormap
# ---------------------------------------------------------------------------
# Create a scatter plot of 300 random 2-D points.
# Colour each point by its distance from the origin.
# Requirements:
# - Use a custom 3-colour segmented colormap:
#     0.0 → 'navy', 0.5 → 'gold', 1.0 → 'firebrick'
#   (hint: mcolors.LinearSegmentedColormap.from_list)
# - Normalise distances to [0, 1]
# - Add a colourbar labelled 'Distance from origin'
# - Title: 'Distance Colormap'
# Save as 'custom_cmap.png'

# YOUR CODE HERE
