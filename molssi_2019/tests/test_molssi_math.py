"""
Unit and regression test for the molssi_math module.
"""

# Import package, test suite, and other packages as needed
import molssi_2019 as ms
import pytest
import sys


@pytest.fixture
def num_list_3():
    return [1, 2, 3, 4, 5]


@pytest.mark.parametrize("num_list, expected_mean", [([1, 2, 3, 4, 5], 3), ([0, 2, 4, 6], 3), ([1, 2, 3, 4], 2.5),
                                                     (list(range(1, 1000000)), 1000000 / 2)])
def test_many(num_list, expected_mean):
    assert ms.mean(num_list) == expected_mean


def test_mean(num_list_3):
    observed = ms.mean(num_list_3)
    expected = 3

    assert observed == expected


def test_mean_type_error():
    test_variable = "this is a string"

    with pytest.raises(TypeError):
        ms.mean(test_variable)


# Skip a test: @pytest.mark.skip
# Label a test: @pytest.mark.test1
# pytest -m "no test1"
def test_mean_zero_length_error():
    test_list = []

    with pytest.raises(ZeroDivisionError):
        ms.mean(test_list)


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass
