
import sys
import pytest

@pytest.mark.skip(reason="doesn't work !!")
def test_skip():
    assert True
    
@pytest.mark.skipif(sys.version_info < (3, 6), reason="Python version too old")
def test_skipif():
    assert True