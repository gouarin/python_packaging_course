import splinart as spl
import numpy as np
import pytest
from pytest import approx

def test_circle_1():
    theta, path = spl.circle([0, 0], 1, npoints=2)

    assert theta == approx([0, 2*np.pi])
    assert path == approx(np.array([[1, 0], [1, 0]]))

def test_circle_2():
    theta, path = spl.circle([0, 0], 1, npoints=5)

    assert theta == approx(np.linspace(0, 2*np.pi, 5))
    assert path == approx(np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [1, 0]]))

def test_line_1():
    path = spl.line(0, 1, npoints=2)

    assert path == approx(np.array([[0, 0.5], [1, 0.5]]))

def test_line_2():
    path = spl.line(0, 1, npoints=3)

    assert path == approx(np.array([[0, 0.5], [0.5, 0.5], [1, 0.5]]))

@pytest.mark.parametrize("nbpoints,expected", [
    (2, np.array([[1, 0], [1, 0]])),
    (5, np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [1, 0]]))
])
def test_circle(nbpoints, expected):
    theta, path = spl.circle([0, 0], 1, npoints=nbpoints)
    assert path == approx(expected)

@pytest.mark.parametrize("nbpoints,expected", [
    (2, np.array([[0, 0.5], [1, 0.5]])),
    (3, np.array([[0, 0.5], [0.5, 0.5], [1, 0.5]]))
])
def test_line(nbpoints, expected):
    path = spl.line(0, 1, npoints=nbpoints)
    assert path == approx(expected)
