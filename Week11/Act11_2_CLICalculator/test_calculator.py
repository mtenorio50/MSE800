import math
import pytest
import calculator


def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0


def test_subtract():
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(-1, -1) == 0


def test_multiply():
    assert calculator.multiply(4, 2) == 8
    assert calculator.multiply(-2, 3) == -6


def test_divide():
    assert calculator.divide(6, 2) == 3
    with pytest.raises(ValueError):
        calculator.divide(5, 0)


def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1


def test_root():
    assert calculator.root(9, 2) == 3
    assert calculator.root(27, 3) == 3
    with pytest.raises(ValueError):
        calculator.root(-16, 2)


def test_sine():
    assert math.isclose(calculator.sine(0), 0)
    assert math.isclose(calculator.sine(math.pi/2), 1)


def test_cosine():
    assert math.isclose(calculator.cosine(0), 1)
    assert math.isclose(calculator.cosine(math.pi), -1)


def test_tangent():
    assert math.isclose(calculator.tangent(0), 0)
    # Do not test tan(pi/2) directly due to infinity
