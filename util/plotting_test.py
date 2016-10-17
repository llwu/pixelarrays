import matplotlib.pyplot as plt

from pixelarrays.util.plotting import plot, coarsen
from pixelarrays.recursive import solve


def paper_example1():
    f = plot(lambda x, w: x * x - w, -2.0, 2.0, -2.0, 2.0)
    fs = coarsen(f)
    plt.imshow(f.T,
               cmap='gray',
               origin='lower',
               interpolation='none',
               extent=[-2, 2, -2, 2])
    plt.show()

    g = plot(lambda w, y: w + y * y - 1, -2.0, 2.0, -2.0, 2.0)
    gs = coarsen(g)
    plt.imshow(gs[5].T,
               cmap='gray',
               origin='lower',
               interpolation='none',
               extent=[-2, 2, -2, 2])
    plt.show()
    s = solve(fs, gs)
    plt.imshow(s.T,
               cmap='gray',
               origin='lower',
               interpolation='none',
               extent=[-2, 2, -2, 2])
    plt.show()

if __name__ == '__main__':
    paper_example1()
