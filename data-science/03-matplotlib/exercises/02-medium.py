"""
Matplotlib — Medium Exercises
==============================
Topics: subplots, styles, customisation, annotations, horizontal bars,
        stacked bars, pie chart.

Run:  python 02-medium.py
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(0)


# ---------------------------------------------------------------------------
# 1. 2×2 subplot grid
# ---------------------------------------------------------------------------
# Create a 2×2 figure (figsize 10×8) with these four plots:
# [0,0] Line: sin(x) and sin(2x) for x in [0, 2π]
# [0,1] Bar: product sales below
# [1,0] Scatter: 50 random points coloured by a third variable z
# [1,1] Histogram: 500 samples from exponential distribution (scale=2)
# Add a shared super-title 'Data Dashboard' (fontsize=14, bold).
# Use plt.tight_layout() and save as '2x2_dashboard.png'.

x   = np.linspace(0, 2 * np.pi, 200)
products = ['A', 'B', 'C', 'D', 'E']
prod_sales = [450, 310, 520, 280, 390]

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Stacked bar chart
# ---------------------------------------------------------------------------
# Plot quarterly revenue for three regions using stacked bars.
# Requirements:
# - Each quarter is a group of bars stacked by region
# - Legend showing the three regions
# - Title: 'Quarterly Revenue by Region'
# - y-label: 'Revenue (R$k)'
# Save as 'stacked_bar.png'

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
north  = [120, 135, 128, 150]
south  = [ 95, 110, 105, 118]
east   = [ 80,  90,  88, 102]

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Annotations and reference lines
# ---------------------------------------------------------------------------
# Plot a noisy sine wave (200 points, amplitude 2, noise std 0.3).
# Requirements:
# - Find and annotate the global maximum with an arrow and 'Peak' label
# - Draw a horizontal dashed line at the mean value
# - Add a shaded band (ax.fill_between) between mean ± 1 std
# - Title: 'Signal with Annotations'
# Save as 'annotated_signal.png'

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Horizontal bar chart — ranked
# ---------------------------------------------------------------------------
# Plot programming language popularity (sorted descending by score).
# Requirements:
# - Horizontal bars sorted so the highest score appears at the top
# - Each bar labelled with its score on the right
# - Title: 'Language Popularity Index'
# - x-label: 'Score'
# Save as 'hbar_ranked.png'

languages = ['Python', 'Java', 'C', 'C++', 'JavaScript', 'Go', 'Rust', 'Kotlin']
scores    = [100, 74, 72, 65, 63, 42, 38, 34]

# YOUR CODE HERE
