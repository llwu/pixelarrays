"""
Baseline algorithm modified to use sparse representation.

Using the CSR layout, matrix-vector multiplication can be done in
O(k) time where k is the number of nonzero elements of the matrix.
[1]

[1] http://gauss.cs.ucsb.edu/~aydin/csb2009.pdf
"""


"""
Baseline algorithm. Just does simple matrix multiplication.
"""

from scipy.sparse import csr_matrix


def solve(f, g):
    """Plots roots (x, y) given plots of f(x, w) and g(w, z)."""
    return csr_matrix(f).dot(csr_matrix(g)).todense()
