# Contributing to Python Projects

Thank you for your interest in contributing! Here are the guidelines to keep the repository clean and consistent.

## How to Contribute

1. **Fork** the repository
2. **Create a branch** with a descriptive name:
   - `feature/list-comprehensions`
   - `fix/typo-variables-readme`
   - `add/mini-project-calculator`
3. Follow the [Content Template](#content-template) below
4. **Open a Pull Request** with a clear description of what you added or changed

## Content Template

Every concept folder must follow this structure:

```
concept-name/
├── README.md
├── notebook.ipynb
├── exercises/
│   ├── 01-easy.py
│   ├── 02-medium.py
│   └── 03-challenge.py
└── solutions/
    ├── 01-easy-solution.py
    └── README-solution.md
```

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use descriptive variable names
- Add comments only where the logic is not self-evident
- Keep exercises self-contained (no external dependencies unless documented)

## Commit Messages

Use the format:

```
Add: <topic> — brief description
Fix: <topic> — what was fixed
Update: <topic> — what changed
```

## Questions

Open an issue with the label `question` and we'll get back to you.
