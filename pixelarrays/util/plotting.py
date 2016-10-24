"""Plotting utilities."""

import numpy as np

SUBD = 2


def plot(f, left, right, bottom, top, granularity=(1024, 1024), epsilon=1e-6):
    """Plots f(x, y) == 0."""
    width = right - left
    height = top - bottom
    prv = np.zeros((granularity[1] + 1,))
    nxt = np.zeros((granularity[1] + 1,))
    output = np.zeros(granularity)
    for y in range(granularity[1] + 1):
        prv[y] = f(left, bottom + height * y / granularity[1])
    for x in range(1, granularity[0] + 1):
        nxt[0] = f(left + width * x / granularity[0], bottom)
        for y in range(1, granularity[1] + 1):
            nxt[y] = f(left + width * x / granularity[0],
                       bottom + height * y / granularity[1])
            if nxt[y] < epsilon:
                if (nxt[y - 1] > -epsilon
                        or prv[y - 1] > -epsilon
                        or prv[y] > -epsilon):
                    output[x - 1][y - 1] = 1
            if nxt[y] > -epsilon:
                if (nxt[y - 1] < epsilon
                        or prv[y - 1] < epsilon
                        or prv[y] < epsilon):
                    output[x - 1][y - 1] = 1
        np.copyto(prv, nxt)
    return output


def _halve(plot):
    """O(1) depth, O(n^2) work."""
    if plot.shape == (1, 1):
        return plot
    if plot.shape[0] % 2 == 1 and plot.shape[0] != 1:
        return np.concatenate((_halve(plot[:-1]), _halve(plot[None, -1, :])))
    elif plot.shape[1] % 2 == 1 and plot.shape[1] != 1:
        return np.concatenate((_halve(plot[:, :-1]),
                               _halve(plot[:, -1, None])),
                              axis=1)
    elif plot.shape[0] == 1:
        view_4d = plot.reshape(1, 1, plot.shape[1] // SUBD, SUBD)
        return np.max(view_4d, axis=(1, 3))
    elif plot.shape[1] == 1:
        view_4d = plot.reshape(plot.shape[0] // SUBD, SUBD, 1, 1)
        return np.max(view_4d, axis=(1, 3))
    else:
        view_4d = plot.reshape(plot.shape[0] // SUBD,
                               SUBD,
                               plot.shape[1] // SUBD,
                               SUBD)
        return np.max(view_4d, axis=(1, 3))


def coarsen(plot):
    """
    Logical ors submatrices, which divides width. Repeat until 1x1.

    O(log n) depth, O(n^2) work via Master Theorem:
    T(n) = T(n/2) + O(n^2)
    """
    if plot.shape == (1, 1):
        return [plot]
    return coarsen(_halve(plot)) + [plot]
