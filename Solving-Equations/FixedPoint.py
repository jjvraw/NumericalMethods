import math

def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    """
    Finds a fixed point of the function g using the Fixed Point Iteration Method.

    Parameters
    ----------
    g : callable
        A Python function that takes a single argument and returns a numerical value.
    x0 : float
        The initial guess for the fixed point.
    tol : float, optional
        The desired tolerance (default 1e-6).
    max_iter : int, optional
        The maximum number of iterations (default 100).

    Returns
    -------
    float
        The fixed point of the function g.

    """
    iters = []
    x = x0

    if is_convergent(g, x0) == False:
        raise ValueError(f"The functionb is not convergent at {x0}.")

    for i in range(max_iter):
        x_new = g(x)
        iters.append([i, x, x_new, abs(x_new - x)]) # i, x, x_new, error
        if abs(x_new - x) < tol:
            return x_new, iters
        x = x_new

    raise ValueError(f"Failed to converge after {max_iter} iterations")

def is_convergent(g, p, eps=1e-6):
    """
    Checks whether the function g is convergent at the fixed point p using the condition |g'(p)| < 1.

    Parameters
    ----------
    g : callable
        A Python function that takes a single argument and returns a numerical value.
    p : float
        The fixed point of g.
    eps : float, optional
        The desired numerical tolerance (default 1e-6).

    Returns
    -------
    bool
        True if g is convergent at p, False otherwise.

    """
    # Compute the derivative of g at p using the central difference formula
    h = math.sqrt(eps)
    g_prime = (g(p + h) - g(p - h)) / (2 * h)

    # Check if the absolute value of the derivative is less than 1
    return abs(g_prime) < 1


if __name__ == "__main__":


    def g(x): 
        return (3*x + 1) / (2*x + 1)
    
    x0 = 0.5
    fixed_pt = fixed_point_iteration(g, x0)[0]

    print(fixed_pt)

    def g_not_convergent(x): 
        return x**2
    
    x0 = 2 
    try:
        fixed_pt = fixed_point_iteration(g_not_convergent, x0)[0]
    except ValueError as e:
        print(e)