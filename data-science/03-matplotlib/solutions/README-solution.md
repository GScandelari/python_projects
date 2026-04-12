# Matplotlib — Solution Notes

## Easy

**Figure/Axes vs pyplot state machine:** Always create figures with `fig, ax = plt.subplots()`. The implicit `plt.plot()` interface is fine for quick exploration but makes subplots and fine-grained control harder.

**Saving before showing:** Call `fig.savefig()` before `plt.show()` — after `show()` the figure may be cleared by the backend.

**Colorbars:** `plt.colorbar(scatter_artist, ax=ax)` maps the artist's normalised values to the colour scale. Set `vmin`/`vmax` on the artist to control the scale.

**`plt.close(fig)`:** Releases memory. In scripts or loops that produce many figures, always close figures you're done with.

## Medium

**Stacked bars:** Pass a `bottom` argument equal to the cumulative sum of previous series. Build it manually (`[a+b for a,b in zip(north, south)]`) or with NumPy: `np.array(north) + np.array(south)`.

**`fill_between`:** Great for confidence intervals, standard deviations, and shaded regions. The `alpha` argument controls transparency.

**Sorting for ranked charts:** `sorted(zip(scores, labels))` gives ascending order. Since horizontal bars are drawn bottom-to-top, ascending input means the highest value ends at the top of the chart.

**`ax.twinx()`:** Creates a second Axes sharing the same x-axis with its own independent y-axis. Call it on the first Axes after it's set up.

## Challenge

**Combined legend for twinx:** Both Axes have independent artists. Extract line handles from each Axes and pass them together to `ax.legend()`.

**Heatmap text colour:** Choose black or white based on cell intensity (`abs(corr) < 0.7 → 'k'`) so the annotation is always readable against the background.

**`sharex=True` in subplots:** All panels zoom and pan together. Ticks appear only on the bottom panel. Set `gridspec_kw={'height_ratios': [...]}` to give different panels different heights.

**`FuncFormatter`:** `ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M'))` formats tick labels without changing the underlying data.

**Custom LinearSegmentedColormap:** `mcolors.LinearSegmentedColormap.from_list('name', ['colour1', 'colour2', ...])` linearly interpolates between the listed colours. Always normalise your data to [0, 1] before applying.
