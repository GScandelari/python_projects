"""
Matplotlib — Easy Exercises
============================
Topics: line plot, bar chart, scatter plot, histogram.

Each exercise asks you to produce a specific figure.
Save each one as a .png file and call plt.show().

Run:  python 01-easy.py
"""

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)


# ---------------------------------------------------------------------------
# 1. Line plot
# ---------------------------------------------------------------------------
# Plot sin(x) and cos(x) on the same Axes for x in [0, 2π].
# Requirements:
# - sin(x) in blue, cos(x) in red dashed line
# - Title: 'Trig Functions'
# - x-label: 'x (radians)', y-label: 'Amplitude'
# - Legend showing 'sin' and 'cos'
# - Horizontal dashed grid at y=0
# Save as 'line_plot.png'

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Bar chart
# ---------------------------------------------------------------------------
# Plot monthly sales using the data below.
# Requirements:
# - Vertical bars with a distinct colour of your choice
# - Add the numeric value as a text label above each bar
# - Title: 'Monthly Sales', y-label: 'Units Sold'
# Save as 'bar_chart.png'

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales  = [320, 285, 410, 390, 450, 370]

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Scatter plot
# ---------------------------------------------------------------------------
# Simulate a dataset: x ~ Uniform(0, 10), y = 1.5*x + noise.
# Use 80 points and np.random.seed(0).
# Requirements:
# - Colour points by their y value using the 'viridis' colormap
# - Add a colourbar with label 'y value'
# - Title: 'Linear Relationship', x-label: 'x', y-label: 'y'
# Save as 'scatter_plot.png'

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Histogram
# ---------------------------------------------------------------------------
# Generate 1 000 samples from a normal distribution (mean=170, std=10).
# Requirements:
# - 25 bins, steelblue colour, white edges
# - Draw a vertical dashed red line at the mean
# - Title: 'Height Distribution'
# - x-label: 'Height (cm)', y-label: 'Count'
# Save as 'histogram.png'

# YOUR CODE HERE
