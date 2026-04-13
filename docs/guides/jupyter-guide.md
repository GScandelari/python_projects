# Jupyter — Guide

## Installation & Launch

```bash
pip install jupyter notebook      # classic notebook
pip install jupyterlab            # JupyterLab (recommended)

jupyter notebook                  # open classic at localhost:8888
jupyter lab                       # open JupyterLab at localhost:8888

# Open specific notebook
jupyter lab path/to/notebook.ipynb

# Run as script (no UI)
jupyter nbconvert --to script notebook.ipynb
jupyter nbconvert --to html   notebook.ipynb
jupyter nbconvert --to pdf    notebook.ipynb
```

---

## Keyboard Shortcuts

### Two modes
- **Command mode** (blue border) — navigate cells. Press `Esc` to enter.
- **Edit mode** (green border) — type inside a cell. Press `Enter` to enter.

### Command mode shortcuts

| Shortcut | Action |
|---|---|
| `↑` / `↓` | Select cell above / below |
| `Enter` | Enter edit mode |
| `A` | Insert cell **above** |
| `B` | Insert cell **below** |
| `D D` | Delete selected cell |
| `Z` | Undo cell deletion |
| `M` | Change to Markdown cell |
| `Y` | Change to Code cell |
| `R` | Change to Raw cell |
| `Shift + ↑/↓` | Select multiple cells |
| `Shift + M` | Merge selected cells |
| `C` | Copy cell |
| `X` | Cut cell |
| `V` | Paste cell below |
| `Shift + L` | Toggle line numbers |
| `O` | Toggle cell output |
| `H` | Show all shortcuts |
| `0 0` | Restart kernel |
| `I I` | Interrupt kernel |

### Edit mode shortcuts

| Shortcut | Action |
|---|---|
| `Shift + Enter` | Run cell + move to next |
| `Ctrl + Enter` | Run cell, stay on it |
| `Alt + Enter` | Run cell + insert below |
| `Ctrl + Z` | Undo in cell |
| `Ctrl + /` | Toggle comment |
| `Tab` | Autocomplete |
| `Shift + Tab` | Docstring popup |
| `Ctrl + Shift + -` | Split cell at cursor |
| `Esc` | Enter command mode |

---

## Magic Commands

Magic commands start with `%` (line magic) or `%%` (cell magic).

### Most useful line magics

```python
%time  sum(range(1_000_000))       # time a single expression
%timeit sum(range(1_000_000))      # average over many runs

%run script.py                     # run a .py file in the notebook namespace
%run -i script.py                  # run with access to current namespace

%load script.py                    # load .py into a cell

%who                               # list all variables
%whos                              # list variables with type + info
%reset                             # delete all variables

%matplotlib inline                 # embed matplotlib in notebook
%matplotlib widget                 # interactive plots (requires ipympl)

%env MY_VAR=hello                  # set environment variable
%env                               # list all env vars

%ls                                # list directory
%pwd                               # print working directory
%cd path/                          # change directory

%history                           # show input history
%history -n 1-10                   # lines 1–10

%pdb on                            # auto-launch debugger on exception
%debug                             # open pdb at last traceback
```

### Most useful cell magics

```python
%%time                             # time the whole cell
%%timeit                           # benchmark the whole cell

%%bash                             # run cell as bash
%%bash
echo "Hello from bash"
ls -la

%%writefile script.py              # write cell content to file
def hello(): print('hello')

%%capture output                   # capture stdout/stderr into `output`
print('captured')

%%html                             # render cell as HTML
<h2 style="color: red">Hello</h2>

%%javascript                       # run cell as JS in browser
console.log('hello from JS')

%%sql                              # SQL (requires ipython-sql + db connection)
SELECT * FROM users LIMIT 5;
```

---

## Display & Rich Output

```python
from IPython.display import display, HTML, Markdown, Image, Javascript

# Markdown in code cell
display(Markdown('## Dynamic heading'))

# HTML
display(HTML('<b style="color:red">Bold red text</b>'))

# Side-by-side DataFrames
display(df1, df2)

# Image
display(Image(filename='chart.png'))
display(Image(url='https://...'))    # remote image

# Multiple outputs in one cell (normally only last is shown)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
```

---

## Working with pandas & matplotlib

```python
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# High-res plots
import matplotlib_inline.backend_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('retina')

# Wide tables
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.float_format', '{:.2f}'.format)

# Progress bar for long operations (requires tqdm)
from tqdm.notebook import tqdm
for i in tqdm(range(1000)):
    pass
```

---

## Notebook as a Script

```python
# Parametrize notebooks with papermill
pip install papermill

# Run with parameters
papermill input.ipynb output.ipynb -p alpha 0.5 -p n_trials 100

# In notebook — mark a cell as "parameters" tag
alpha = 0.1      # default, overridden by papermill
n_trials = 10
```

---

## nbconvert — Export Options

```bash
jupyter nbconvert notebook.ipynb --to html
jupyter nbconvert notebook.ipynb --to pdf        # requires LaTeX
jupyter nbconvert notebook.ipynb --to script     # → .py
jupyter nbconvert notebook.ipynb --to markdown
jupyter nbconvert notebook.ipynb --to slides     # reveal.js slideshow
jupyter nbconvert notebook.ipynb --execute       # run, then convert
jupyter nbconvert notebook.ipynb --no-input      # hide code, show output
```

---

## Useful Extensions

| Extension | Purpose | Install |
|---|---|---|
| `nbstripout` | Remove cell output before git commit | `pip install nbstripout` |
| `nbformat` | Validate / manipulate notebook files | built-in with Jupyter |
| `papermill` | Parametrize + execute notebooks | `pip install papermill` |
| `tqdm` | Progress bars | `pip install tqdm` |
| `ipywidgets` | Interactive sliders / dropdowns | `pip install ipywidgets` |
| `jupytext` | Sync `.ipynb` ↔ `.py` files | `pip install jupytext` |

---

## Tips & Gotchas

| Issue | Fix |
|---|---|
| Kernel restart loses variables | Re-run all cells from top (`Kernel → Restart & Run All`) |
| Output cluttered | `Cell → All Output → Clear` |
| Notebook not saving | Check disk space; use `File → Save` (Ctrl+S) |
| `import` changes not reflected | Restart kernel after editing a module |
| asyncio in Jupyter | `await coro()` works directly (Jupyter runs an event loop) |
| `multiprocessing` may hang | Use `spawn` start method or run in terminal instead |
| Large notebooks slow to load | Clear outputs before saving; use `nbstripout` |
