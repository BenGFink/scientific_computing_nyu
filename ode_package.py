# ODE solver package for the final in sci comp with jonathan goodman at NYU
# made by benajmin fink

import numpy as np

"""
 _______ these are the definitions I used for each argument________
method ---- the technique being used to approximate the ode, (in our case either euler or runge kutta 4th)
f  ---- the function defining the first order autonomous explicit ode 
x0 ---- the initial values/ state of the ode
dt ---- the time step used
T ---- the end time of the calculation
    """


def solve_ODE(method, f, x0, dt, T):
    # produces a sequence of frames where each frame is the update of the previous one
    xk = x0
    framesInfo = [x0]  # make sure that the first frame is the initial values x0
    time = 0  # we always start at time 0

    while time < T:
        xk = method(f, xk, dt)  # method here is either runge kutta or euler
        framesInfo.append(xk)
        time = time + dt

    return framesInfo


def eulerStep(f, xk, dt):
    f1 = f(xk)
    xk1 = xk + dt * f1
    return xk1


def rungeKuttaStep(f, xk, dt):
    f1 = f(xk)
    f2 = f(xk + (dt / 2) * f1)
    f3 = f(xk + (dt / 2) * f2)
    f4 = f(xk + dt * f3)
    xk1 = xk + (dt / 6) * (f1 + 2 * f2 + 2 * f3 + f4)
    return xk1


def error_analysis(method, T, func, x0, solution):
    errorlist = []
    dt = .01
    for i in range(10):
        instance = solve_ODE(method, func, x0, dt, T).pop()
        error = solution(T) - instance
        errorlist.append(error)
        dt = dt / 2
    return errorlist


def convergence_test(list, i):
    output = []
    for j in range(len(list) - 2):
        ratio = np.log2(list[j][i] / list[j + 1][i])
        output.append(ratio)
    return output


def adaptive_dt(epsilon, dtguess, order, method, func, x0, T):
    dt = dtguess
    count = 0
    while count < 16:  # maximum number of times to try before giving up

        instance = solve_ODE(method, func, x0, dt, T).pop()
        next_instance = solve_ODE(method, func, x0, dt / 2, T).pop()
        estimated_error = (instance - next_instance) / (2 ** order - 1)

        if np.linalg.norm(estimated_error) <= epsilon:
            return [dt, instance + estimated_error]

        dt = dt / 2
        count = count + 1

    print("ERROR message___reached max iterations___ giving up")
    return
