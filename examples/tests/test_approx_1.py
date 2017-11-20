
from pytest import approx

def test_approx_1():
    assert 1.001 == approx(1)
    
def test_approx_2():
    assert 1.001 == approx(1, rel=1e-3)