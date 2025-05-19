import pytest

from mypackage import add, div, mul, sub


@pytest.mark.parametrize(
    ("a", "b", "answer"),
    [
        (1, 2, 3),
        (1, -1, 0),
        (10, 100, 110),
    ],
)
def test_add(a: float, b: float, answer: float) -> None:
    """Test add function."""
    result = add(a, b)
    assert result == answer


@pytest.mark.parametrize(
    ("a", "b", "answer"),
    [
        (1, 2, -1),
        (1, -1, 2),
        (10, 100, -90),
    ],
)
def test_sub(a: float, b: float, answer: float) -> None:
    """Test sub function."""
    result = sub(a, b)
    assert result == answer


@pytest.mark.parametrize(
    ("a", "b", "answer"),
    [
        (1, 2, 2),
        (1, -1, -1),
        (10, 100, 1000),
    ],
)
def test_mul(a: float, b: float, answer: float) -> None:
    """Test mul function."""
    result = mul(a, b)
    assert result == answer


@pytest.mark.parametrize(
    ("a", "b", "answer"),
    [
        (1, 2, 0.5),
        (1, -1, -1),
        (10, 100, 0.1),
    ],
)
def test_div(a: float, b: float, answer: float) -> None:
    """Test div function."""
    result = div(a, b)
    assert result == answer


@pytest.mark.parametrize("a", [1, -1, 0])
def test_div_zero(a: float) -> None:
    """Test divide by zero."""
    with pytest.raises(ZeroDivisionError):
        _ = div(a, 0)
