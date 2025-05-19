"""functions."""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """Calculate a + b.

    Args:
        a (float): left hand side
        b (float): right hand side

    Returns:
        result (float): Sum of a and b.
    """
    return a + b


def sub(a: float, b: float) -> float:
    """Calculate a - b.

    Args:
        a (float): left hand side
        b (float): right hand side

    Returns:
        result (float)
    """
    return a - b


def mul(a: float, b: float) -> float:
    """Calculate a * b.

    Args:
        a (float): left hand side
        b (float): right hand side

    Returns:
        result (float)
    """
    return a * b


def div(a: float, b: float = 1) -> float:
    """Calculate a / b.

    Args:
        a (float): left hand side
        b (float): right hand side

    Returns:
        result (float)
    """
    return a / b
