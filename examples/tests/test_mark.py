
import pytest

@pytest.mark.slow
def test_slow():
    assert True
    
def test_not_slow():
    assert True