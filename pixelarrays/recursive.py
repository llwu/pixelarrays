"""Recursive array multiplication algorithm."""

import numpy as np

from pixelarrays.util.plotting import SUBD


def _solve(f, g, i, j, k, output):
    if len(f) == 0 or len(g) == 0:
        output[i][j] = 1
        return
    for i2 in range(i * SUBD, (i + 1) * SUBD):
        if i2 >= f[0].shape[0]:
            break
        for j2 in range(j * SUBD, (j + 1) * SUBD):
            if j2 >= g[0].shape[1]:
                break
            for k2 in range(k * SUBD, (k + 1) * SUBD):
                if k2 >= f[0].shape[1] or k2 >= g[0].shape[0]:
                    break
                if f[0][i2][k2] * g[0][k2][j2] > 1e-3:
                    _solve(f[1:], g[1:], i2, j2, k2, output)


def solve(f, g):
    """Plots roots (x, y) given coarsened plots of f(x, w) and g(w, z)."""
    output = np.zeros(f[-1].shape)
    _solve(f, g, 0, 0, 0, output)
    return output
