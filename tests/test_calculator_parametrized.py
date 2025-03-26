import pytest
from src import calculator

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1,3,4),
        (0,5,5),
        (-2, 9, 7),
        (5,-8,-3),
    ]
)


def test_add_parametrized(a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (1,3,4),
        (0,5,5),
        (-2, 9, 7),
        (5,-8,-3),
    ]
)

def test_add_wrong_parametrized(x, y, expected_result):
    assert calculator.add_wrong(x, y) == expected_result

@pytest.mark.parametrize(
    "s, d, expected_result_1",
    [
        (1,3,4),
        (0,5,5),
        (-2, 9, 7),
        (5,-8,-3),
    ]
)

def test_subtract_parametrized(s, d, expected_result_1):
    assert calculator.subtract(s, d) == expected_result_1

@pytest.mark.parametrize(
    "q, w, expected_result_2",
    [
        (1,3,4),
        (0,5,5),
        (-2, 9, 7),
        (5,-8,-3),
    ]
)

def test_multiply_parametrized(q, w, expected_result_2):
    assert calculator.multiply(q, w) == expected_result_2

@pytest.mark.parametrize(
    "e, r, expected_result_3",
    [
        (1,3,4),
        (0,5,5),
        (-2, 9, 7),
        (5,-8,-3),
    ]
)

def test_multiply_wrong_parametrized(e, r, expected_result_3):
    assert calculator.multiply_wrong(e, r) == expected_result_3

@pytest.mark.parametrize(
    "t, z, expected_result_4",
    [
        (1,3,4),
        (0,5,5),
        (-2, 9, 7),
        (5,-8,-3),
    ]
)

def test_divide_parametrized(t, z, expected_result_4):
    assert calculator.divide(t, z) == expected_result_4


@pytest.mark.parametrize(
    "a, b, expected_expection, expected_msg",
    [
        (0, 5, ValueError, "Cannot take log of non-positive number!"),
        (-2, 5, ValueError, "Cannot take log of non-positive number!"),
        (9, -2, ZeroDivisionError, "Cannot take log with non-positive base!"),
        (5, 1, NameError, "Cannot take log with base 1!"),
    ],
)
def test_log(a, b, expected_expection, expected_msg):
    with pytest.raises(expected_expection) as exc:
        calculator.log(a, b)
    assert str(exc.value) == expected_msg