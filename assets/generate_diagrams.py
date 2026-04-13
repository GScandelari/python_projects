"""
Generate visual assets for the Python Projects repository.

Run:  python assets/generate_diagrams.py
Output: PNG files saved inside assets/

Requirements:
    pip install matplotlib numpy
"""

import matplotlib
matplotlib.use('Agg')   # non-interactive backend — safe for scripts

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
DARK_BG   = '#1a1a2e'
CARD_BG   = '#16213e'
CARD2_BG  = '#0f3460'
BLUE      = '#3776ab'
YELLOW    = '#ffd43b'
GREEN     = '#68d391'
RED       = '#fc8181'
PURPLE    = '#b794f4'
ORANGE    = '#f6ad55'
TEAL      = '#4fd1c5'
GRAY      = '#718096'
WHITE     = '#f7fafc'
LIGHT     = '#a0aec0'


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------
def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f'  Saved {name}')


def dark_fig(w, h):
    fig = plt.figure(figsize=(w, h), facecolor=DARK_BG)
    return fig


# ---------------------------------------------------------------------------
# 1. Learning Roadmap
# ---------------------------------------------------------------------------
def roadmap():
    fig = dark_fig(14, 8)
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(DARK_BG)
    ax.set_xlim(0, 14); ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(7, 7.4, 'Learning Roadmap', ha='center', va='center',
            fontsize=22, fontweight='bold', color=WHITE, fontfamily='monospace')

    columns = [
        {'x': 1.4,  'color': GREEN,  'title': 'BEGINNER',
         'items': ['01 Fundamentals', '02 Control Flow', '03 Data Structures',
                   '04 Functions', '05 Strings', 'Mini-Projects']},
        {'x': 4.2,  'color': BLUE,   'title': 'INTERMEDIATE',
         'items': ['01 OOP', '02 Modules & Packages', '03 File Handling',
                   '04 Error Handling', '05 Comprehensions', 'Mini-Projects']},
        {'x': 7.0,  'color': PURPLE, 'title': 'ADVANCED',
         'items': ['01 Decorators & Generators', '02 Concurrency & Async',
                   '03 Testing (pytest)', '04 Design Patterns', 'Capstone Projects']},
        {'x': 9.8,  'color': ORANGE, 'title': 'DATA SCIENCE',
         'items': ['NumPy', 'Pandas', 'Matplotlib']},
        {'x': 11.9, 'color': TEAL,   'title': 'EXTRAS',
         'items': ['FastAPI', 'Flask', 'Requests / BS4', 'Automation']},
    ]

    for col in columns:
        x, color = col['x'], col['color']
        # Column header
        header = FancyBboxPatch((x - 1.1, 6.3), 2.2, 0.7,
                                boxstyle='round,pad=0.08', linewidth=0,
                                facecolor=color, alpha=0.9)
        ax.add_patch(header)
        ax.text(x, 6.67, col['title'], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=DARK_BG)

        # Items
        for i, item in enumerate(col['items']):
            y = 5.7 - i * 0.88
            card = FancyBboxPatch((x - 1.05, y - 0.28), 2.1, 0.56,
                                  boxstyle='round,pad=0.05', linewidth=1,
                                  edgecolor=color, facecolor=CARD_BG, alpha=0.85)
            ax.add_patch(card)
            ax.text(x, y, item, ha='center', va='center',
                    fontsize=7.5, color=WHITE)

        # Arrow to next column
        if x < 11.0:
            next_x = columns[columns.index(col) + 1]['x']
            ax.annotate('', xy=(next_x - 1.1, 6.67), xytext=(x + 1.1, 6.67),
                        arrowprops=dict(arrowstyle='->', color=LIGHT,
                                        lw=1.5, connectionstyle='arc3,rad=0'))

    save(fig, 'roadmap.png')


# ---------------------------------------------------------------------------
# 2. Python Data Types
# ---------------------------------------------------------------------------
def data_types():
    fig = dark_fig(12, 7)
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(DARK_BG)
    ax.set_xlim(0, 12); ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(6, 6.5, 'Python Built-in Types', ha='center', va='center',
            fontsize=20, fontweight='bold', color=WHITE, fontfamily='monospace')

    categories = [
        {'x': 1.4, 'color': BLUE,   'title': 'Numeric',
         'items': [('int',   'Whole numbers'),
                   ('float', 'Decimal numbers'),
                   ('complex','Real + imaginary')]},
        {'x': 3.8, 'color': GREEN,  'title': 'Text',
         'items': [('str',   'Immutable sequence'),
                   ('f-string','Formatted literal'),
                   ('bytes', 'Binary data')]},
        {'x': 6.2, 'color': PURPLE, 'title': 'Sequence',
         'items': [('list',  'Mutable, ordered'),
                   ('tuple', 'Immutable, ordered'),
                   ('range', 'Integer sequence')]},
        {'x': 8.6, 'color': ORANGE, 'title': 'Mapping / Set',
         'items': [('dict',  'Key → value'),
                   ('set',   'Unique, unordered'),
                   ('frozenset','Immutable set')]},
        {'x': 11.0,'color': TEAL,   'title': 'Other',
         'items': [('bool',  'True / False'),
                   ('None',  'Null value'),
                   ('bytes', 'Binary sequence')]},
    ]

    for cat in categories:
        x, color = cat['x'], cat['color']
        header = FancyBboxPatch((x - 1.1, 5.4), 2.2, 0.65,
                                boxstyle='round,pad=0.08', linewidth=0,
                                facecolor=color, alpha=0.85)
        ax.add_patch(header)
        ax.text(x, 5.73, cat['title'], ha='center', va='center',
                fontsize=10, fontweight='bold', color=DARK_BG)

        for i, (name, desc) in enumerate(cat['items']):
            y = 4.55 - i * 1.25
            card = FancyBboxPatch((x - 1.05, y - 0.48), 2.1, 0.96,
                                  boxstyle='round,pad=0.05', linewidth=1,
                                  edgecolor=color, facecolor=CARD_BG, alpha=0.8)
            ax.add_patch(card)
            ax.text(x, y + 0.15, name, ha='center', va='center',
                    fontsize=10, fontweight='bold', color=color, fontfamily='monospace')
            ax.text(x, y - 0.18, desc, ha='center', va='center',
                    fontsize=8, color=LIGHT)

    save(fig, 'data_types.png')


# ---------------------------------------------------------------------------
# 3. OOP Concepts
# ---------------------------------------------------------------------------
def oop_concepts():
    fig = dark_fig(13, 8)
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(DARK_BG)
    ax.set_xlim(0, 13); ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(6.5, 7.5, 'OOP Concepts', ha='center', va='center',
            fontsize=20, fontweight='bold', color=WHITE, fontfamily='monospace')

    def class_box(ax, x, y, title, subtitle, attrs, methods, color, w=2.4, h=3.2):
        box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                             boxstyle='round,pad=0.1', linewidth=2,
                             edgecolor=color, facecolor=CARD_BG)
        ax.add_patch(box)
        # Title bar
        bar = FancyBboxPatch((x - w/2, y + h/2 - 0.55), w, 0.55,
                             boxstyle='round,pad=0.05', linewidth=0,
                             facecolor=color, alpha=0.85)
        ax.add_patch(bar)
        ax.text(x, y + h/2 - 0.28, title, ha='center', va='center',
                fontsize=10, fontweight='bold', color=DARK_BG)
        if subtitle:
            ax.text(x, y + h/2 - 0.72, subtitle, ha='center', va='center',
                    fontsize=8, color=GRAY, style='italic')
        # Divider
        ax.plot([x - w/2 + 0.1, x + w/2 - 0.1],
                [y + h/2 - 0.85, y + h/2 - 0.85], color=color, lw=0.8, alpha=0.5)
        top = y + h/2 - 1.1
        for attr in attrs:
            ax.text(x - w/2 + 0.15, top, attr, va='center',
                    fontsize=8, color=LIGHT, fontfamily='monospace')
            top -= 0.32
        ax.plot([x - w/2 + 0.1, x + w/2 - 0.1],
                [top - 0.05, top - 0.05], color=color, lw=0.8, alpha=0.5)
        top -= 0.28
        for meth in methods:
            ax.text(x - w/2 + 0.15, top, meth, va='center',
                    fontsize=8, color=GREEN, fontfamily='monospace')
            top -= 0.32

    # Animal (parent)
    class_box(ax, 6.5, 5.8, 'Animal', '(Base Class)',
              ['+ name: str', '+ sound: str'],
              ['+ speak()', '+ __str__()'],
              BLUE)

    # Dog (child)
    class_box(ax, 3.5, 2.4, 'Dog', '(inherits Animal)',
              ['+ breed: str'],
              ['+ speak()', '+ fetch()'],
              GREEN)

    # Cat (child)
    class_box(ax, 9.5, 2.4, 'Cat', '(inherits Animal)',
              ['+ indoor: bool'],
              ['+ speak()', '+ purr()'],
              PURPLE)

    # Arrows (inheritance)
    ax.annotate('', xy=(3.5, 4.2), xytext=(5.3, 4.7),
                arrowprops=dict(arrowstyle='<|-', color=GREEN, lw=2))
    ax.annotate('', xy=(9.5, 4.2), xytext=(7.7, 4.7),
                arrowprops=dict(arrowstyle='<|-', color=PURPLE, lw=2))

    ax.text(4.0, 4.6, 'extends', fontsize=9, color=GRAY, style='italic')
    ax.text(8.5, 4.6, 'extends', fontsize=9, color=GRAY, style='italic')

    # Pillars
    pillars = [
        (1.4, 1.3, BLUE,   'Encapsulation', 'Bundle data + behaviour\nHide internal details'),
        (4.2, 1.3, GREEN,  'Inheritance',   'Reuse parent behaviour\nExtend or override'),
        (7.0, 1.3, PURPLE, 'Polymorphism',  'Same interface\nDifferent behaviour'),
        (9.8, 1.3, ORANGE, 'Abstraction',   'Expose what matters\nHide the rest'),
    ]
    for px, py, pc, pt, pd in pillars:
        pill = FancyBboxPatch((px - 1.2, py - 0.7), 2.4, 1.4,
                              boxstyle='round,pad=0.1', linewidth=1.5,
                              edgecolor=pc, facecolor=CARD2_BG)
        ax.add_patch(pill)
        ax.text(px, py + 0.32, pt, ha='center', va='center',
                fontsize=9, fontweight='bold', color=pc)
        ax.text(px, py - 0.22, pd, ha='center', va='center',
                fontsize=7.5, color=LIGHT, multialignment='center')

    save(fig, 'oop_concepts.png')


# ---------------------------------------------------------------------------
# 4. Concurrency Models
# ---------------------------------------------------------------------------
def concurrency():
    fig = dark_fig(13, 7)
    ax  = fig.add_axes([0.04, 0.1, 0.92, 0.82])
    ax.set_facecolor(DARK_BG)
    fig.patch.set_facecolor(DARK_BG)
    ax.set_xlim(0, 13); ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(6.5, 6.6, 'Python Concurrency Models', ha='center', va='center',
            fontsize=20, fontweight='bold', color=WHITE, fontfamily='monospace')

    cols = [
        {'x': 2.5, 'color': GREEN,  'title': 'threading',
         'subtitle': 'I/O-bound tasks',
         'pros': ['Simple to use', 'Shared memory', 'GIL released on I/O'],
         'cons': ['GIL limits CPU work', 'Race conditions', 'Harder to debug'],
         'use': 'Network requests\nFile I/O\nWeb scraping',
         'code': 'Thread(target=fn)\nLock()\nThreadPoolExecutor'},
        {'x': 6.5, 'color': BLUE,   'title': 'asyncio',
         'subtitle': 'Many I/O tasks',
         'pros': ['Single thread', 'Very low overhead', 'Scales to thousands'],
         'cons': ['Requires async libs', 'Learning curve', 'Not for CPU work'],
         'use': 'APIs & WebSockets\nAsync databases\nHigh concurrency',
         'code': 'async def / await\nasyncio.gather()\nasyncio.Queue'},
        {'x': 10.5,'color': ORANGE, 'title': 'multiprocessing',
         'subtitle': 'CPU-bound tasks',
         'pros': ['Bypasses GIL', 'True parallelism', 'Full CPU utilisation'],
         'cons': ['High memory use', 'IPC overhead', 'No shared state'],
         'use': 'Data crunching\nImage processing\nML training',
         'code': 'Pool(processes=N)\npool.map(fn, data)\nProcess()'},
    ]

    for col in cols:
        x, color = col['x'], col['color']
        # Card background
        card = FancyBboxPatch((x - 1.9, 0.4), 3.8, 5.9,
                              boxstyle='round,pad=0.12', linewidth=2,
                              edgecolor=color, facecolor=CARD_BG, alpha=0.9)
        ax.add_patch(card)

        # Header
        hdr = FancyBboxPatch((x - 1.9, 5.75), 3.8, 0.55,
                             boxstyle='round,pad=0.08', linewidth=0,
                             facecolor=color, alpha=0.9)
        ax.add_patch(hdr)
        ax.text(x, 6.03, col['title'], ha='center', va='center',
                fontsize=13, fontweight='bold', color=DARK_BG, fontfamily='monospace')
        ax.text(x, 5.5, col['subtitle'], ha='center', va='center',
                fontsize=9, color=color, style='italic')

        # Pros
        ax.text(x, 5.1, '✓ Pros', ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=GREEN)
        for i, pro in enumerate(col['pros']):
            ax.text(x, 4.75 - i * 0.35, f'+ {pro}', ha='center', va='center',
                    fontsize=8, color=LIGHT)

        ax.plot([x - 1.7, x + 1.7], [3.55, 3.55], color=GRAY, lw=0.6, alpha=0.5)

        # Cons
        ax.text(x, 3.35, '✗ Cons', ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=RED)
        for i, con in enumerate(col['cons']):
            ax.text(x, 3.0 - i * 0.35, f'- {con}', ha='center', va='center',
                    fontsize=8, color=LIGHT)

        ax.plot([x - 1.7, x + 1.7], [1.82, 1.82], color=GRAY, lw=0.6, alpha=0.5)

        # Use cases
        ax.text(x, 1.62, 'Use for', ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=color)
        ax.text(x, 1.18, col['use'], ha='center', va='center',
                fontsize=8, color=LIGHT, multialignment='center')

        ax.plot([x - 1.7, x + 1.7], [0.7, 0.7], color=GRAY, lw=0.6, alpha=0.5)

        # Code snippet
        ax.text(x, 0.55, col['code'], ha='center', va='center',
                fontsize=7.5, color=YELLOW, fontfamily='monospace',
                multialignment='center')

    save(fig, 'concurrency_models.png')


# ---------------------------------------------------------------------------
# 5. Design Patterns Map
# ---------------------------------------------------------------------------
def design_patterns():
    fig = dark_fig(14, 8)
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(DARK_BG)
    ax.set_xlim(0, 14); ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(7, 7.5, 'Design Patterns', ha='center', va='center',
            fontsize=22, fontweight='bold', color=WHITE, fontfamily='monospace')

    categories = [
        {'x': 2.3, 'color': GREEN,  'title': 'CREATIONAL',
         'subtitle': 'Object creation',
         'patterns': [
             ('Singleton',  'One shared instance'),
             ('Factory',    'Create without knowing class'),
             ('Builder',    'Step-by-step construction'),
         ]},
        {'x': 7.0, 'color': BLUE,   'title': 'STRUCTURAL',
         'subtitle': 'Object composition',
         'patterns': [
             ('Decorator',  'Add behaviour at runtime'),
             ('Adapter',    'Convert one interface to another'),
             ('Facade',     'Simplified unified interface'),
         ]},
        {'x': 11.7,'color': PURPLE, 'title': 'BEHAVIOURAL',
         'subtitle': 'Object communication',
         'patterns': [
             ('Observer',   'Notify on state change'),
             ('Strategy',   'Swap algorithms at runtime'),
             ('Command',    'Encapsulate requests / undo'),
             ('Template',   'Skeleton + variable steps'),
         ]},
    ]

    for cat in categories:
        x, color = cat['x'], cat['color']
        # Category header
        hdr = FancyBboxPatch((x - 2.0, 6.3), 4.0, 0.85,
                             boxstyle='round,pad=0.1', linewidth=0,
                             facecolor=color, alpha=0.85)
        ax.add_patch(hdr)
        ax.text(x, 6.82, cat['title'], ha='center', va='center',
                fontsize=12, fontweight='bold', color=DARK_BG)
        ax.text(x, 6.48, cat['subtitle'], ha='center', va='center',
                fontsize=9, color=DARK_BG, alpha=0.8)

        for i, (name, desc) in enumerate(cat['patterns']):
            y = 5.4 - i * 1.35
            card = FancyBboxPatch((x - 1.85, y - 0.48), 3.7, 0.96,
                                  boxstyle='round,pad=0.08', linewidth=1.5,
                                  edgecolor=color, facecolor=CARD_BG, alpha=0.85)
            ax.add_patch(card)
            # Colour dot
            ax.add_patch(plt.Circle((x - 1.5, y), 0.12, color=color, zorder=5))
            ax.text(x - 1.1, y + 0.16, name, va='center',
                    fontsize=10, fontweight='bold', color=WHITE, fontfamily='monospace')
            ax.text(x - 1.1, y - 0.18, desc, va='center',
                    fontsize=8.5, color=LIGHT)

    # When-to-use footer
    footer_y = 0.55
    ax.text(7, footer_y, 'Choose by intent: Creational → how objects are made   '
            'Structural → how they are composed   '
            'Behavioural → how they communicate',
            ha='center', va='center', fontsize=9, color=GRAY, style='italic')

    save(fig, 'design_patterns.png')


# ---------------------------------------------------------------------------
# 6. Data Science Workflow
# ---------------------------------------------------------------------------
def data_science_workflow():
    fig = dark_fig(14, 5)
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(DARK_BG)
    ax.set_xlim(0, 14); ax.set_ylim(0, 5)
    ax.axis('off')

    ax.text(7, 4.6, 'Data Science Workflow', ha='center', va='center',
            fontsize=20, fontweight='bold', color=WHITE, fontfamily='monospace')

    steps = [
        {'x': 1.2,  'color': BLUE,   'num': '01', 'title': 'Collect',
         'tool': 'requests\nBeautifulSoup\nCSV / JSON',
         'desc': 'Fetch or load\nraw data'},
        {'x': 3.5,  'color': TEAL,   'num': '02', 'title': 'Clean',
         'tool': 'pandas\ndropna, fillna\nstr.strip()',
         'desc': 'Handle missing\nvalues & types'},
        {'x': 5.8,  'color': GREEN,  'num': '03', 'title': 'Explore',
         'tool': 'pandas\nmatplotlib\ndescribe()',
         'desc': 'Understand\ndistributions'},
        {'x': 8.1,  'color': PURPLE, 'num': '04', 'title': 'Transform',
         'tool': 'numpy\npandas\ngroupby / merge',
         'desc': 'Feature\nengineering'},
        {'x': 10.4, 'color': ORANGE, 'num': '05', 'title': 'Visualise',
         'tool': 'matplotlib\nseaborn\nplotly',
         'desc': 'Communicate\nfindings'},
        {'x': 12.7, 'color': YELLOW, 'num': '06', 'title': 'Report',
         'tool': 'Jupyter\nPDF / HTML\nJSON export',
         'desc': 'Document and\nshare results'},
    ]

    for i, step in enumerate(steps):
        x, color = step['x'], step['color']
        card = FancyBboxPatch((x - 1.0, 0.4), 2.0, 3.8,
                              boxstyle='round,pad=0.1', linewidth=2,
                              edgecolor=color, facecolor=CARD_BG, alpha=0.9)
        ax.add_patch(card)

        # Number badge
        ax.add_patch(plt.Circle((x, 3.9), 0.3, color=color, zorder=5))
        ax.text(x, 3.9, step['num'], ha='center', va='center',
                fontsize=9, fontweight='bold', color=DARK_BG, zorder=6)

        ax.text(x, 3.35, step['title'], ha='center', va='center',
                fontsize=11, fontweight='bold', color=WHITE)

        ax.text(x, 2.65, step['desc'], ha='center', va='center',
                fontsize=8, color=LIGHT, multialignment='center')

        ax.plot([x - 0.8, x + 0.8], [2.2, 2.2], color=color, lw=0.6, alpha=0.4)

        ax.text(x, 1.55, step['tool'], ha='center', va='center',
                fontsize=8, color=color, fontfamily='monospace',
                multialignment='center')

        # Arrow to next step
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + 1.15, 2.3), xytext=(x + 1.0, 2.3),
                        arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.5))

    save(fig, 'data_science_workflow.png')


# ---------------------------------------------------------------------------
# 7. Web API Flow (FastAPI / Flask)
# ---------------------------------------------------------------------------
def web_api_flow():
    fig = dark_fig(13, 6)
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(DARK_BG)
    ax.set_xlim(0, 13); ax.set_ylim(0, 6)
    ax.axis('off')

    ax.text(6.5, 5.6, 'REST API Request/Response Cycle', ha='center', va='center',
            fontsize=18, fontweight='bold', color=WHITE, fontfamily='monospace')

    def box(ax, x, y, w, h, title, lines, color, code=None):
        b = FancyBboxPatch((x - w/2, y - h/2), w, h,
                           boxstyle='round,pad=0.1', linewidth=2,
                           edgecolor=color, facecolor=CARD_BG)
        ax.add_patch(b)
        hdr = FancyBboxPatch((x - w/2, y + h/2 - 0.42), w, 0.42,
                             boxstyle='round,pad=0.05', linewidth=0,
                             facecolor=color, alpha=0.85)
        ax.add_patch(hdr)
        ax.text(x, y + h/2 - 0.21, title, ha='center', va='center',
                fontsize=9.5, fontweight='bold', color=DARK_BG)
        top = y + h/2 - 0.65
        for line in lines:
            ax.text(x, top, line, ha='center', va='center', fontsize=8, color=LIGHT)
            top -= 0.32
        if code:
            ax.text(x, y - h/2 + 0.32, code, ha='center', va='center',
                    fontsize=8, color=color, fontfamily='monospace')

    def arrow(ax, x1, y1, x2, y2, label='', color=GRAY):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))
        if label:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + 0.18
            ax.text(mx, my, label, ha='center', fontsize=8, color=color)

    # Flow: Client → Route → Validation → Handler → Response → Client
    box(ax, 1.3,  3.0, 2.2, 2.4, 'Client',
        ['HTTP Request', 'GET / POST / PUT', 'DELETE', 'Headers + Body'], TEAL)

    box(ax, 3.9,  4.2, 2.2, 1.6, 'Router',
        ['Match URL pattern', 'Check HTTP method'], BLUE,
        '@app.get("/items")')

    box(ax, 3.9,  1.8, 2.2, 1.6, 'Middleware',
        ['Auth check', 'Rate limiting', 'Logging'], PURPLE,
        'before_request()')

    box(ax, 6.8,  3.0, 2.4, 2.4, 'Handler',
        ['Business logic', 'Validate input', 'Call service/DB', 'Build response'], GREEN,
        'def endpoint(...):\n  return data')

    box(ax, 9.8,  4.2, 2.2, 1.6, 'Pydantic',
        ['Validate types', 'Serialize output'], ORANGE,
        'response_model=')

    box(ax, 9.8,  1.8, 2.2, 1.6, 'Error Handler',
        ['4xx Client errors', '5xx Server errors'], RED,
        '@app.errorhandler()')

    box(ax, 12.2, 3.0, 1.6, 2.4, 'Response',
        ['JSON body', 'Status code', 'Headers'], TEAL)

    # Arrows
    arrow(ax, 2.4,  3.6, 2.8, 3.9,  'request',  TEAL)
    arrow(ax, 2.4,  2.4, 2.8, 2.1,  '',         TEAL)
    arrow(ax, 5.0,  4.2, 5.6, 3.4,  '',         BLUE)
    arrow(ax, 5.0,  1.8, 5.6, 2.6,  '',         PURPLE)
    arrow(ax, 8.0,  3.6, 8.7, 4.2,  '',         GREEN)
    arrow(ax, 8.0,  2.4, 8.7, 1.8,  '',         GREEN)
    arrow(ax, 10.9, 4.2, 11.4, 3.6, 'response', ORANGE)
    arrow(ax, 10.9, 1.8, 11.4, 2.4, '',         RED)

    save(fig, 'web_api_flow.png')


# ---------------------------------------------------------------------------
# Run all
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    print('Generating assets...')
    roadmap()
    data_types()
    oop_concepts()
    concurrency()
    design_patterns()
    data_science_workflow()
    web_api_flow()
    print(f'\nAll diagrams saved to {OUT}/')
