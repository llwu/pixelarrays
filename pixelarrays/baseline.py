"""
Baseline algorithm. Just does simple matrix multiplication.
"""

from numpy import dot


def solve(f, g):
    """Plots roots (x, y) given plots of f(x, w) and g(w, z)."""
    return dot(f, g)
