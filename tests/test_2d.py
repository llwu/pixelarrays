"""Tests plotting the solutions to 2D equations."""

from time import clock

import matplotlib.pyplot as plt
from numpy.random import randint

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
    # granularity = (randint(1000, 2000), randint(1000, 2000), randint(1000, 2000))
    granularity = (4096, 4096, 4096)

    start = clock()
    f = plot(lambda x, w: x * x - w, -2.0, 2.0, -2.0, 2.0,
             granularity=(granularity[0], granularity[1]))
    end = clock()
    print(end - start)
    show_plot(f)

    start = clock()
    g = plot(lambda w, y: w + y * y - 1, -2.0, 2.0, -2.0, 2.0,
             granularity=(granularity[1], granularity[2]))
    end = clock()
    print(end - start)
    show_plot(g)

    start = clock()
    s = solve(f, g)
    end = clock()
    print(end - start)
    show_plot(s)

if __name__ == '__main__':
    paper_example1()
