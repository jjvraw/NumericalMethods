import mpmath as mp
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
        The number of nodes in [a,b]. Must be odd and greater than 2 since we map the interval [a,b] to [x_0, x_n-1].

    Returns
    -------
    float
        The approximate value of the definite integral.

    """
    if n % 2 == 0:
        raise ValueError("n must be odd")
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
    approx_integral = composite_simpson(f, a, b, n)
    print(f"n = {n} -> integral = {approx_integral}, abs error: {abs(approx_integral - exact_integral)}")

    n = 1001
    approx_integral = composite_simpson(f, a, b, n)
    print(f"n = {n} -> integral = {approx_integral}, abs error: {abs(approx_integral - exact_integral)}")

    n = 5001
    approx_integral = composite_simpson(f, a, b, n)
    print(f"n = {n} -> integral = {approx_integral}, abs error: {abs(approx_integral - exact_integral)}")

    n = 10001
    approx_integral = composite_simpson(f, a, b, n)
    print(f"n = {n} -> integral = {approx_integral}, abs error: {abs(approx_integral - exact_integral)}")

    n = 50001
    approx_integral = composite_simpson(f, a, b, n)
    print(f"n = {n} -> integral = {approx_integral}, abs error: {abs(approx_integral - exact_integral)}")