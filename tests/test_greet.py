from python_survivor import greet


def test_greet_default() -> None:
    assert greet() == "Hello, gopher! Welcome to Python."


def test_greet_name() -> None:
    assert greet("Ada") == "Hello, Ada! Welcome to Python."
