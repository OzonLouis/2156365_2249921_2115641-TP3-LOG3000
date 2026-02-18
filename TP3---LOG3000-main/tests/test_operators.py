"""Tests for arithmetic operator helpers."""

from operators import add, subtract, multiply, divide


def test_add():
    """Return the sum of two numbers."""
    assert add(2, 3) == 5


def test_subtract():
    """Return left minus right operand."""
    assert subtract(10, 4) == 6


def test_multiply():
    """Return the product of two numbers."""
    assert multiply(6, 7) == 42


def test_divide():
    """Return the quotient of two numbers."""
    assert divide(8, 2) == 4


def test_divide_decimal():
    """Return the decimal quotient when division has a remainder."""
    assert divide(7, 2) == 3.5
