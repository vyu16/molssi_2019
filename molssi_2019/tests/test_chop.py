"""
Unit and regression test for the chop module.
"""

# Import package, test suite, and other packages as needed
import molssi_2019 as ms
import pytest
import sys


@pytest.mark.parametrize("target, num_list, expected_id", [(3, [], -1), (3, [1], -1), (1, [1], 0), (1, [1, 3, 5], 0),
                                                           (3, [1, 3, 5], 1), (5, [1, 3, 5], 2), (0, [1, 3, 5], -1),
                                                           (2, [1, 3, 5], -1), (4, [1, 3, 5], -1), (6, [1, 3, 5], -1),
                                                           (1, [1, 3, 5, 7], 0), (3, [1, 3, 5, 7], 1),
                                                           (5, [1, 3, 5, 7], 2), (7, [1, 3, 5, 7], 3),
                                                           (0, [1, 3, 5, 7], -1), (2, [1, 3, 5, 7], -1),
                                                           (4, [1, 3, 5, 7], -1), (6, [1, 3, 5, 7], -1),
                                                           (8, [1, 3, 5, 7], -1)])
@pytest.mark.parametrize("test_method", [ms.chop1, ms.chop2])
@pytest.mark.chop
@pytest.mark.skip
def test_chop(target, num_list, expected_id, test_method):
    assert test_method(target, num_list) == expected_id
