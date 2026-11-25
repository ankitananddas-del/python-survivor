# python-survivor

A week-long Python toolchain bootcamp for Go developers. The project uses
[uv](https://docs.astral.sh/uv/) for environments and dependencies,
[ruff](https://docs.astral.sh/ruff/) for linting and formatting,
[mypy](https://mypy.readthedocs.io/) in strict mode for type checking, and
[pytest](https://docs.pytest.org/) for tests. All of their settings are in
[`pyproject.toml`](pyproject.toml).

New to Python and coming from Go? Start with [GO_TO_PYTHON.md](GO_TO_PYTHON.md).

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) 0.13 or newer
  (`curl -LsSf https://astral.sh/uv/install.sh | sh`)

You don't need to install Python yourself. uv downloads the version pinned in
`.python-version` (3.12) if it isn't already available.

## Setup

```bash
git clone <repo-url> python-survivor
cd python-survivor
uv sync            # creates .venv and installs runtime + dev dependencies from uv.lock
```

## Running the checks

| Check | Command | What it does |
|---|---|---|
| Tests | `uv run pytest` | Runs everything under `tests/` |
| Lint | `uv run ruff check .` | Lints with the rule sets in `[tool.ruff.lint]` |
| Lint + autofix | `uv run ruff check --fix .` | Applies safe fixes (import order, etc.) |
| Format check | `uv run ruff format --check .` | Fails if any file isn't formatted |
| Format | `uv run ruff format .` | Rewrites files in place |
| Type check | `uv run mypy` | Strict mode over `src/` and `tests/` (paths come from `[tool.mypy].files`) |

Run everything at once, as CI would:

```bash
uv sync --frozen && \
uv run ruff check . && \
uv run ruff format --check . && \
uv run mypy && \
uv run pytest
```

## Layout

```
.
├── pyproject.toml          # project metadata + ruff / mypy / pytest config
├── uv.lock                 # pinned dependency versions (commit this)
├── .python-version         # interpreter version uv uses
├── src/python_survivor/    # the package (py.typed marks it as typed)
├── tests/                  # pytest tests
└── GO_TO_PYTHON.md         # Go → Python command cheat sheet
```
