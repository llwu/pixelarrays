"""Tests plotting the solutions to 2D equations."""

from time import clock

import matplotlib.pyplot as plt

from pixelarrays.util.plotting import plot, coarsen
from pixelarrays.recursive import solve

def show_plot(f):
    plt.imshow(f.T,
               cmap='gray',
               origin='lower',
               interpolation='none',
               extent=[-2, 2, -2, 2])
    plt.show()


def paper_example1():
    """Tests example from https://arxiv.org/pdf/1609.00061v1.pdf."""
    start = clock()
    f = plot(lambda x, w: x * x - w, -2.0, 2.0, -2.0, 2.0)
    end = clock()
    print(end - start)
    show_plot(f)

    start = clock()
    g = plot(lambda w, y: w + y * y - 1, -2.0, 2.0, -2.0, 2.0)
    end = clock()
    print(end - start)
    show_plot(g)

    start = clock()
    fs = coarsen(f)
    end = clock()
    print(end - start)

    start = clock()
    gs = coarsen(g)
    end = clock()
    print(end - start)

    start = clock()
    s = solve(fs, gs)
    end = clock()
    print(end - start)
    show_plot(s)

if __name__ == '__main__':
    paper_example1()
