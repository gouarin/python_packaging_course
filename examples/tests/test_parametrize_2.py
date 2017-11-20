
import pytest

from fibonacci import *

@pytest.mark.parametrize('value1', range(5))
@pytest.mark.parametrize('value2', range(0,10,2))  
def test_methods(value1, value2):
    assert not (value1*value2 & 1)