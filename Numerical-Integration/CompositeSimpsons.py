import math

import numpy as np


def composite_simpson(f, a, b, n):
    """
    Computes the definite integral of f(x) over the interval [a, b] using the Composite Simpson's Rule
    with n evenly spaced points.

    Parameters
    ----------
    f : callable
        A Python function that takes a single argument and returns a numerical value.
    a : float
        The lower bound of the interval.
    b : float
        The upper bound of the interval.
    n : int
        The number of subintervals (must be even).

    Returns
    -------
    float
        The approximate value of the definite integral.

    """
    if n % 2 != 0:
        raise ValueError("n must be even")

    h = (b - a) / n
    x = [a + i*h for i in range(n+1)]
    y = [f(x_i) for x_i in x]

    integral = (h/3) * (y[0] + 4*sum(y[1:n:2]) + 2*sum(y[2:n:2]) + y[n])
    return integral

if __name__ == "__main__":
    f = lambda x: math.sqrt(1+x**4) / x**2
    a = 1
    b = 2
    h = 0.01
    n = len(np.arange(a, b, h))
    approx_integral = composite_simpson(f, a, b, n)
    print(f"h = {h} -> integral = {approx_integral}, abs error: {abs(approx_integral - 1.132090393305915)}")

    h = 0.005
    n = len(np.arange(a, b, h))
    approx_integral = composite_simpson(f, a, b, n)
    print(f"h = {h} -> integral = {approx_integral}, abs error: {abs(approx_integral - 1.132090393305915)}")

    h = 0.00025
    n = len(np.arange(a, b, h))
    approx_integral = composite_simpson(f, a, b, n)
    print(f"h = {h} -> integral = {approx_integral}, abs error: {abs(approx_integral - 1.132090393305915)}")