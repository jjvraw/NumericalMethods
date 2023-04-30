import math


def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Finds a root of the function f using the Bisection Method.

    Parameters
    ----------
    f : callable
        A Python function that takes a single argument and returns a numerical value.
    a : float
        The lower bound of the initial interval.
    b : float
        The upper bound of the initial interval.
    tol : float, optional
        The desired tolerance (default 1e-6).
    max_iter : int, optional
        The maximum number of iterations (default 100).

    Returns
    -------
    tuple (float, list)
        The root of the function f, and a list of intermediate values at each iteration.

    Raises
    ------
    ValueError
        If the signs of f(a) and f(b) are the same.

    """
    iters = []
    i = 0
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs - range not good.")

    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        iters.append([i, a, b, c, fc, (b-a)/2]) # i, a, b, c, f(c), solution_error
        if abs(fc) < tol:
            return c, iters
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    raise ValueError(f"Failed to converge after {max_iter} iterations")


if __name__ =="__main__":

    def f(t): 
        return 8 - 4.5*(t - math.sin(t)) 
    a = 2
    b = 3
    try:
        approx_root, iters = bisection(f, a, b)
        print(f"The root is: {approx_root}")
    except ValueError as e:
        print(e)


    f = lambda x: 6*x + 5 - math.sin(x)
    a = -1
    b = 0
    try:
        approx_root, iters = bisection(f, a, b)
        print(f"The root is: {approx_root}")
    except ValueError as e:
        print(e)