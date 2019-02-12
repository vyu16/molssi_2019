"""
Unit and regression test for the string_util.py module.
"""

# Import package, test suite, and other packages as needed
import molssi_2019 as ms
import pytest
import sys

# Skip a test: @pytest.mark.skip
# Label a test: @pytest.mark.test1
# pytest -m "no test1"


@pytest.fixture
def test_str():
    return "molecular SCienCE SOFTWARE insTITUte"


@pytest.fixture
def result_str():
    return "Molecular Science Software Institute"


@pytest.mark.parametrize("strings, results", [("XXX", "Xxx"), ("xxx YYY", "Xxx Yyy"), ("Xxx yYy zzZ", "Xxx Yyy Zzz")])
def test_many(strings, results):
    assert ms.title_case(strings) == results


def test_title_case(test_str, result_str):
    assert ms.title_case(test_str) == result_str


def test_title_case_type_error():
    with pytest.raises(TypeError):
        ms.title_case(1)


def test_title_case_zero_length_error():
    with pytest.raises(ValueError):
        ms.title_case("")
