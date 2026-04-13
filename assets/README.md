# Assets

Visual aids and diagrams for the Python Projects repository.

## Files

| File | Description |
|---|---|
| `banner.svg` | Repository banner — used in the main README |
| `generate_diagrams.py` | Script that generates all PNG diagrams |
| `roadmap.png` | Full learning path from Beginner to Extras |
| `data_types.png` | Python built-in types overview |
| `oop_concepts.png` | OOP pillars and class diagram example |
| `concurrency_models.png` | threading vs asyncio vs multiprocessing |
| `design_patterns.png` | Creational / Structural / Behavioural patterns map |
| `data_science_workflow.png` | 6-step data science workflow |
| `web_api_flow.png` | REST API request/response cycle |

## Regenerating diagrams

```bash
pip install matplotlib numpy
python assets/generate_diagrams.py
```

All PNGs are saved directly into the `assets/` folder.
