"""
Recursive array multiplication algorithm. Requires nonnegative
matrices. Requires coarsening which costs O(nm + mp) space and O(nm +
mp) time. Runs in O(log n + log m + log p) depth and O(sum k_i) work on
top of that, where k_i is the number of triples (x, y, z) with A_i[x][z]
* B_i[z][y] > 0 and A_i and B_i are the ith coarsened matrices.

Thus, this algorithm is suited to mid-sized matrices with mid or
less sparsity. For smaller matrices consider simple matrix
multiplication. For larger matrices, the space bottleneck will
necessitate sparse matrix multiplication.
"""

import numpy as np

from pixelarrays.util.plotting import SUBD, coarsen


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
    """Plots roots (x, y) given plots of f(x, w) and g(w, z)."""
    f = coarsen(f)
    g = coarsen(g)
    output = np.zeros((f[-1].shape[0], g[-1].shape[1]))
    _solve(f, g, 0, 0, 0, output)
    return output
