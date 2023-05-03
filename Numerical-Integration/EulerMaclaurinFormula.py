import numpy as np
from CompositeTrapezium import composite_trapezium
import math
import mpmath as mp

if __name__ == "__main__": 
    
    f = lambda x: np.sqrt(1+x**4) / x**2
    df = lambda x: -2 / (x**3 * math.sqrt(1 + x**4)) 
    h = 0.01
    n = len(np.arange(1, 2, h))
    trap = composite_trapezium(f, 1, 2, n)
    exact = float(mp.quad(f, [1, 2]))
    err = abs(exact - trap)
    err_estimate = (h**2 / 12) * (df(2) - df(1))

    print(f"Error: {err}, Error Estimate: {err_estimate}")

    err_of_error_estimate = abs(err_estimate - err)
    print(f"Error of Error Estimate: {err_of_error_estimate}")

    print(f"Intergral approximation: {trap}, Exact: {exact}, Error: {err}")
    trap_with_endpoint = trap - err_estimate
    print(f"Intergral approximation with endpoint correction: {trap_with_endpoint}, Error: {abs(exact - trap_with_endpoint)}")