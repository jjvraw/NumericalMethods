def newtons_method(f, df, x0, tol=1e-6, max_iter=100):
    """
    Finds a root of the function f using Newton's Method.

    Parameters
    ----------
    f : callable
        A Python function that takes a single argument and returns a numerical value.
    df : callable
        The derivative of f.
    x0 : float
        The initial guess for the root.
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
        If the algorithm fails to converge.

    """
    iters = []
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        dx = fx / dfx
        iters.append([i, x, fx, dfx, dx]) # i, x, f(x), f'(x), dx
        if abs(dx) < tol:
            return x, iters
        x -= dx
    raise ValueError(f"Failed to converge after {max_iter} iterations")


if __name__ == "__main__":
    def f(x):
        return (x-1) * (x**2 + 3)
    
    def df(x):
        return 3 * x**2 + 2 * x - 1
    
    x0 = 2
    try:
        approx_root, iters = newtons_method(f, df, x0)
        print(f"The root is: {approx_root}")
    except ValueError as e:
        print(e)

    f = lambda x: x**2 - 2
    df = lambda x: 2*x
    x0 = 1
    try:
        approx_root, iters = newtons_method(f, df, x0)
        print(f"The root is: {approx_root}")
    except ValueError as e:
        print(e)