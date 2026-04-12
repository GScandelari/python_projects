# Capstone Project 2 — Full Test Suite

Write a complete pytest test suite for a small but realistic banking module. You receive the production code — your job is to achieve full coverage with well-structured tests.

## Concepts Used

| Concept | Where |
|---|---|
| pytest fixtures + scopes | Test setup |
| Parametrize | Edge-case coverage |
| Mocking + patch | Isolate external dependencies |
| tmp_path | File-based tests |
| pytest.raises + match | Exception testing |

## Structure

```
02-test-suite/
  bank.py         ← production code (do not modify)
  test_bank.py    ← your test file (skeleton)
  solution_test_bank.py ← full reference test suite
```

## How to Run

```bash
pip install pytest pytest-cov
pytest solution_test_bank.py -v --tb=short
pytest solution_test_bank.py --cov=bank --cov-report=term-missing
```

## Learning Goals

- Write tests that catch real bugs, not just happy paths
- Use fixtures to avoid duplication without losing clarity
- Achieve >90% coverage on a realistic module
- Understand the difference between testing behaviour vs implementation
