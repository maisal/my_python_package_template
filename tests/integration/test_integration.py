from mypackage import add, div, mul, sub


def test_chained_operations() -> None:
    """Calculate (2+3)*4+10//2"""
    step1 = add(2, 3)
    step2 = mul(step1, 4)
    step3 = div(10, 2)
    result = sub(step2, step3)

    assert result == 15


def test_complex_expression() -> None:
    """Calculate (7*3)-(10//2)+1"""
    part1 = mul(7, 3)
    part2 = div(10, 2)
    part3 = sub(part1, part2)
    result = add(part3, 1)

    assert result == 17
