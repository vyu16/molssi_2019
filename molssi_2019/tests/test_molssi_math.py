"""
Unit and regression test for the molssi_math module.
"""

# Import package, test suite, and other packages as needed
import molssi_2019 as ms
import pytest
import sys


def test_mean():
    num_list = [1, 2, 3, 4, 5]
    observed = ms.mean(num_list)
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
