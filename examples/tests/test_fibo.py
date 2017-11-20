import sys
sys.path.append("./examples/tests")
import pytest

from fibonacci import *

@pytest.mark.parametrize('fact_number, expected', [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def test_methods(fact_number, expected):
    assert factorielle(fact_number) == expected