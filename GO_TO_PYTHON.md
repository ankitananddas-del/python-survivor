# Go → Python command cheat sheet

Everyday Go commands and the `uv` / `ruff` / `mypy` / `pytest` commands that do
the same job in this repository. Prefix tool commands with `uv run` so they
use the project's locked virtual environment, much like `go` uses the module
cache pinned by `go.sum`.

| Go command | Python equivalent | Note |
|---|---|---|
| `go mod init example.com/app` | `uv init --lib app` | Creates `pyproject.toml` (≈ `go.mod`) and a `src/` package layout. |
| `go get github.com/x/y` | `uv add y` | Adds the dependency to `pyproject.toml`, updates `uv.lock` (≈ `go.sum`), and installs it. |
| `go get -tool …` / test-only deps | `uv add --dev pytest` | Dev-only dependencies go in `[dependency-groups].dev` and are left out of the built package. |
| `go mod tidy` | `uv lock` then `uv sync` | `uv lock` re-resolves the lockfile; `uv sync` makes `.venv` match it exactly and removes anything extra. |
| `go mod download` | `uv sync --frozen` | Installs exactly what's in `uv.lock` without re-resolving (what you want in CI). |
| `go build ./...` | `uv build` | Builds an sdist and a wheel into `dist/`. You get a distributable package, not a native binary. |
| `go run ./cmd/app` | `uv run python -m python_survivor` | Runs code inside the project env. `uv run <script>` also works for a single file. |
| `go test ./...` | `uv run pytest` | Finds `tests/test_*.py`. Use `-k name` to filter, like `go test -run`. |
| `go test -v -run TestX` | `uv run pytest -v -k test_x` | `-k` matches names by substring or expression. |
| `go test -cover` | `uv run pytest --cov` | Needs `pytest-cov` (`uv add --dev pytest-cov`). |
| `go vet ./...` | `uv run ruff check .` | Lints for bugs and suspicious code. Rule sets are chosen in `[tool.ruff.lint]`. |
| `gofmt -w .` / `goimports` | `uv run ruff format .` + `uv run ruff check --fix .` | `format` sets the layout. `check --fix` sorts imports (rule `I`) and applies safe auto-fixes. |
| `gofmt -l .` (CI check) | `uv run ruff format --check .` | Exits non-zero if any file would be reformatted. |
| *(compiler type checking)* | `uv run mypy` | Python isn't type-checked at build time. `mypy --strict` is the closest thing to the Go compiler rejecting bad types. |
| `go version` | `uv run python --version` | The interpreter version is pinned in `.python-version` and `requires-python`. |
| `go env GOPATH` / `go list -m all` | `uv tree` | Shows the resolved dependency graph. |
| `go install golang.org/x/tools/…@latest` | `uv tool install ruff` | Installs a CLI globally in its own isolated environment. |
| `go clean -cache -testcache` | `uv cache clean` | Clears uv's download/build cache. Delete `.venv` and `.*_cache/` dirs for a full reset. |

## Mental-model mapping

| Go concept | Python / uv concept |
|---|---|
| `go.mod` | `pyproject.toml` |
| `go.sum` | `uv.lock` (commit it) |
| module cache / `vendor/` | `.venv/` (don't commit it; `uv sync` rebuilds it) |
| package = directory | package = directory containing `__init__.py` |
| `internal/` | a leading underscore (`_private.py`) by convention only; nothing enforces it |
| `_test.go` files next to code | `tests/test_*.py` in a separate directory |
