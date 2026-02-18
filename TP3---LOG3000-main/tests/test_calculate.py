"""Tests for expression parsing and evaluation."""

import pytest

from app import calculate


def test_calculate_addition():
    """Check that addition expressions are evaluated correctly."""
    assert calculate("2+3") == 5


def test_calculate_subtraction():
    """Check that subtraction expressions are evaluated correctly."""
    assert calculate("10-4") == 6


def test_calculate_multiplication():
    """Check that multiplication expressions are evaluated correctly."""
    assert calculate("6*7") == 42


def test_calculate_division():
    """Check that division expressions are evaluated correctly."""
    assert calculate("8/2") == 4


def test_calculate_division_decimal():
    """Check that division with remainder returns decimal result."""
    assert calculate("7/2") == 3.5


def test_calculate_rejects_multiple_operators():
    """Reject expressions with more than one operator."""
    with pytest.raises(ValueError):
        calculate("1+2+3")


def test_calculate_rejects_missing_operands():
    """Reject expressions missing a left or right operand."""
    with pytest.raises(ValueError):
        calculate("+2")
    with pytest.raises(ValueError):
        calculate("2+")


def test_calculate_rejects_non_numeric_operands():
    """Reject expressions with non-numeric operands."""
    with pytest.raises(ValueError):
        calculate("a+2")
