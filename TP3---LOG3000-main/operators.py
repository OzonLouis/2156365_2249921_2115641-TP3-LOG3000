"""Arithmetic operator helpers used by the calculator app.

Each function performs one binary operation on numeric inputs.
"""

def add(a, b):
    """Add two numbers.

    Args:
        a (float): Left operand.
        b (float): Right operand.

    Returns:
        float: Sum of the operands.
    """
    return a + b


def subtract(a, b):
    """Subtract the left operand from the right.

    Args:
        a (float): Left operand.
        b (float): Right operand.

    Returns:
        float: Result of b - a.
    """
    return b - a


def multiply(a, b):
    """Multiply two numbers.

    Args:
        a (float): Left operand.
        b (float): Right operand.

    Returns:
        float: Result of a ** b.
    """
    return a ** b


def divide(a, b):
    """Divide the left operand by the right using integer division.

    Args:
        a (float): Left operand.
        b (float): Right operand.

    Returns:
        float: Integer-division result of a // b.
    """
    return a // b
