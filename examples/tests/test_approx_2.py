
import numpy as np
import pytest
from pytest import approx

def ones_array(shape):
    return np.ones(shape)

@pytest.fixture(params=[5, (3,2), (5, 4, 3)])
def init_array(request):
    return ones_array(request.param)
    
def test_approx(init_array):
    shape = init_array.shape
    random_array = 1 + 1e-5*np.random.random(shape)
    assert random_array == approx(init_array, rel=1e-5)