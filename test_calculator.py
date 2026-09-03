import numpy as np
from calculator import calculate, create_matrix, powfix


def test_calculate():
    # multiplication test
    matrix = np.array([[1, 2], [4, 5]])
    result = calculate(matrix, "mpy 3")
    expected = np.array([[3, 6], [12, 15]])
    assert np.array_equal(result, expected)

    # transposition test
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    result = calculate(matrix, "trs")
    expected = np.array([[1, 4], [2, 5], [3, 6]])
    assert np.array_equal(result, expected)

    # determinant test
    matrix = np.array([[1, 2], [4, 5]])
    result = calculate(matrix, "det")
    expected = -3.0
    assert np.array_equal(result, expected)


def test_powfix():
    matrix = np.array([[1, 2], [4, 5]])
    result = powfix(matrix, 2)
    expected = np.array([[9, 12], [24, 33]])
    assert np.array_equal(result, expected)


def test_create_matrix(monkeypatch):
    input = iter(["2", "1 2", "4 5"])
    monkeypatch.setattr("builtins.input", lambda *args: next(input))
    result = create_matrix()
    expected = np.array([[1, 2], [4, 5]])
    assert np.array_equal(result, expected)
