import math

def secant(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Finds a root of the function f using the Secant Method.

    Parameters
    ----------
    f : callable
        A Python function that takes a single argument and returns a numerical value.
    x0 : float
        The first initial guess.
    x1 : float
        The second initial guess.
    tol : float, optional
        The desired tolerance (default 1e-6).
    max_iter : int, optional
        The maximum number of iterations (default 100).

    Returns
    -------
    float
        The root of the function f.

    Raises
    ------
    ValueError
        If the Secant Method fails to converge.

    """
    iters = []
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        dx = (x1 - x0) / (fx1 - fx0) * fx1
        iters.append([i, x1, fx1, dx])
        if abs(dx) < tol:
            return x1, iters
        x0 = x1
        x1 = x1 - dx

    raise ValueError(f"Failed to converge after {max_iter} iterations")


if __name__ == "__main__":
    def f(theta): 
        return theta - math.sin(theta) - 8/4.5
    x0 = 1/2 * math.pi
    x1 = math.pi 
    try: 
        root, iters = secant(f, x0, x1)
        print(f"The root is {root}.")
    except ValueError as e:
        print(e)

    f = lambda x: x**2 - 2
    x0 = 1
    x1 = 2
    try:
        root, iters = secant(f, x0, x1)
        print(f"The root is {root}.")
    except ValueError as e:
        print(e)

    f = lambda x: x**3 - 2*x - 2
    x0 = 1
    x1 = 2
    try:
        root, iters = secant(f, x0, x1)
        print(f"The root is {root}.")
    except ValueError as e:
        print(e)

    print(iters)