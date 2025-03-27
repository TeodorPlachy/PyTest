import pytest
from src import calculatorUkol

@pytest.mark.parametrize(
    "a, b, c, expected_expection, expected_msg",
    [
        ("string", 4, 4, TypeError, "All coefficients must be of type float or int!"),
        (0, 4, 4, SyntaxError, "Cannot solve quadratic formula with a = 0!"),
        (9, 5, 0, NameError, "I don't like when b = 5!"),
        (4, 4, 999999, ValueError, "Cannot solve quadratic formula with negative discriminant!"),
    ],
)

def test_solve_quadratic_formula_errors(a, b, c, expected_expection, expected_msg):
    with pytest.raises(expected_expection) as exc:
        calculatorUkol.solve_quadratic_formula(a, b, c)
    assert str(exc.value) == expected_msg

@pytest.mark.parametrize(
    "a, b, c, result",
    [
        (2, 28, 0, (0, -14)),
        (1, -5, 6, (3, 2)),
        (1, -7, 10, (5, 2)),
    ],
)

def test_solve_quadratic_formula(a, b, c, result):
    assert calculatorUkol.solve_quadratic_formula(a, b, c) == result