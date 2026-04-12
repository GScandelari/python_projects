# Capstone Project 3 — Pattern Library

Build a reusable mini-library that combines all four advanced concepts into a cohesive system: a configurable event-driven data pipeline.

## Concepts Used

| Concept | Where |
|---|---|
| Decorators | `@stage`, `@retry`, `@timed` |
| Generators | Lazy data sources and transformers |
| Design Patterns | Observer (events), Strategy (filtering/sorting), Builder (pipeline config) |
| Testing | Full pytest suite in `test_pipeline.py` |

## Architecture

```
PipelineBuilder (Builder)
  └── Pipeline
        ├── source: Generator function
        ├── stages: [callable]  — each stage is a generator transformer
        ├── sink: callable
        └── EventEmitter (Observer) — fires on item_processed, error, complete
```

## Structure

```
03-pattern-library/
  pipeline.py          ← production code (skeleton)
  solution_pipeline.py ← reference implementation
  test_pipeline.py     ← test suite (skeleton)
  solution_test_pipeline.py ← reference tests
```

## How to Run

```bash
python solution_pipeline.py
pytest solution_test_pipeline.py -v
```

## Learning Goals

- Combine multiple patterns in a single coherent design
- Think about API ergonomics (how easy is it to use?)
- Write tests for code that uses generators and callbacks
