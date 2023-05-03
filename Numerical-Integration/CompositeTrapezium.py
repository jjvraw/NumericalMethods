import mpmath as mp
from scipy.integrate import quad
import numpy as np


def composite_trapezium(f, a, b, n):
    """
    Computes the definite integral of f(x) over the interval [a, b] using the Composite Trapezium Rule
    with n evenly spaced nodes.
    Parameters
    ----------
    f : callable
        A Python function that takes a single argument and returns a numerical value.
    a : float
        The lower bound of the interval.
    b : float
        The upper bound of the interval.
    n : int
        The number of nodes in [a,b]

    Returns
    -------
    float
        The approximate value of the definite integral.

    """
    h = (b - a) / (n - 1)
    x = np.linspace(a, b, n)
    y = f(x)

    result = y[0] + y[-1]
    result += 2 * np.sum(y[1:-1])

    return (h / 2) * result


if __name__ == "__main__":

    f = lambda x: np.sqrt(1+x**4) / x**2
    a = 1
    b = 2
    exact_integral = mp.quad(f, [1, 2])

    n = 101
    approx_integral = composite_trapezium(f, a, b, n)
    print(f"n = {n} -> integral = {approx_integral}, abs error: {abs(approx_integral - exact_integral)}")

    n = 1001
    approx_integral = composite_trapezium(f, a, b, n)
    print(f"n = {n} -> integral = {approx_integral}, abs error: {abs(approx_integral - exact_integral)}")

    n = 5001
    approx_integral = composite_trapezium(f, a, b, n)
    print(f"n = {n} -> integral = {approx_integral}, abs error: {abs(approx_integral - exact_integral)}")

    n = 10001
    approx_integral = composite_trapezium(f, a, b, n)
    print(f"n = {n} -> integral = {approx_integral}, abs error: {abs(approx_integral - exact_integral)}")

    n = 50001
    approx_integral = composite_trapezium(f, a, b, n)
    print(f"n = {n} -> integral = {approx_integral}, abs error: {abs(approx_integral - exact_integral)}")