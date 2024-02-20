import numpy as np


def func_problem1(x):
    scalar = (np.pi / np.sqrt(x[0] ** 2 + x[1] ** 2))
    vector = np.array([-x[1], x[0]])
    f = scalar * vector
    return f


def expected_solution(T):
    pi = np.pi
    y0 = np.cos(pi * T)
    y1 = np.sin(pi * T)
    x = np.array([y0, y1])
    return x


















