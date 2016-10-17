import numpy as np

SUBD = 2


def plot(f, left, right, bottom, top, granularity=2048, epsilon=1e-6):
    """Plots f(x, y) == 0."""
    width = right - left
    height = top - bottom
    prv = np.zeros((granularity + 1,))
    nxt = np.zeros((granularity + 1,))
    output = np.zeros((granularity, granularity))
    for y in range(granularity + 1):
        prv[y] = f(left, bottom + height * y / granularity)
    for x in range(1, granularity + 1):
        nxt[0] = f(left + width * x / granularity, bottom)
        for y in range(1, granularity + 1):
            nxt[y] = f(left + width * x / granularity,
                       bottom + height * y / granularity)
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


def coarsen(plot):
    """Logical ors submatrices, which divides width. Repeat until 1x1."""
    if plot.shape[0] <= 1:
        return [plot]
    view_4d = plot.reshape(plot.shape[0] // SUBD,
                           SUBD,
                           plot.shape[1] // SUBD,
                           SUBD)
    coarse = np.max(view_4d, axis=(1, 3))
    return coarsen(coarse) + [plot]
