import math
import numpy as np
import mpmath as mp

def romberg_integration(f, a, b, n):
    """
    Computes the definite integral of f(x) from a to b using the Romberg integration method.

    Parameters
    ----------
    f : callable
        A Python function that takes a single argument and returns a numerical value.
    a : float
        The lower bound of the integration interval.
    b : float
        The upper bound of the integration interval.
    n : int
        The number of iterations to perform.

    Returns
    -------
    float
        The approximate value of the definite integral of f(x) from a to b.
    """
    R = np.zeros((n,n))
    h = b - a
    R[0, 0] = (h/2.0) * (f(a) + f(b))
    for j in range(1, n):
        h = h / 2.0
        R[j, 0] = 0.5 * R[j-1, 0] + h * np.sum([f(a + (2*k-1)*h) for k in range(1, 2**(j-1)+1)])
        for k in range(1, j+1):
            R[j, k] = (4**k * R[j, k-1] - R[j-1, k-1]) / (4**k - 1)

    return R[-1,-1], R


if __name__ == "__main__": 
    f = lambda x: math.log(x)
    a = 1
    b = 2
    n = 4
    exact = float(mp.quad(f, [a, b]))
    approx_integral, R = romberg_integration(f, a, b, n)
    print(f"Integral = {approx_integral}, abs error: {abs(approx_integral - exact)}")
    np.set_printoptions(precision=10)
    print(np.array(R))