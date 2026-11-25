"""python-survivor: a Go developer's Python toolchain bootcamp."""

__all__ = ["greet"]


def greet(name: str = "gopher") -> str:
    """Return a friendly greeting for ``name``."""
    return f"Hello, {name}! Welcome to Python."
