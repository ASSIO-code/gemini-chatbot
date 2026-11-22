---
trigger: glob
globs: "*.py, **/pyproject.toml, **/requirements*.txt"
description: "Enforce using uv for Python execution, virtual environments, and package management."
---

# Python Execution & Package Management Rule

- **Always use `uv`**: Never run `python`, `pip`, or `venv` directly. All Python execution, virtual environment creation, and dependency management must go through `uv`.
- **Default Python Version**: Use Python 3.12 (`--python 3.12` when creating environments or running versions).
- **Execution & Dependencies**:
  - Run scripts: `uv run ...`
  - Manage packages: `uv add`, `uv remove`, `uv pip ...`
  - Virtual environments: `uv venv`
