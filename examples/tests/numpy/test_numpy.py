import numpy as np
import pytest

@pytest.mark.npz_compare
def test_npz_arange():
    return np.arange(10)

@pytest.mark.npz_compare
def test_npz_two_arange():
    return np.arange(10), np.arange(30)

@pytest.mark.npz_compare(rel=1e-6)
def test_npz_random():
    return 1 + 1e-5*np.random.random(10)