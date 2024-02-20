
import ode_package as ode
import matplotlib.pyplot as plt
import problem_1_package as p1

x0 = [1, 0]

eulerError = ode.error_analysis(ode.eulerStep, 2, p1.func_problem1, x0, p1.expected_solution)
eulerErrConv = ode.convergence_test(eulerError,0)

plt.plot(eulerError)
plt.title('euler error')
plt.ylabel('absolute error')
plt.show()

plt.plot(eulerErrConv)
plt.title('euler order of accuracy')
plt.ylabel('log of consecutive error ratios')
plt.show()


rungeKuttaError = ode.error_analysis(ode.rungeKuttaStep, 10, p1.func_problem1, x0, p1.expected_solution)
rungeKuttaErrConv = ode.convergence_test(rungeKuttaError)

plt.plot(rungeKuttaError)
plt.title('runge kutta error')
plt.ylabel('absolute error')
plt.show()

plt.plot(rungeKuttaErrConv)
plt.title('runge kutta order of accuracy')
plt.ylabel('log of consecutive error ratios')
plt.show()

def extract_frames(list):
    return [item[0] for item in list], \
           [item[1] for item in list]


euler = ode.solve_ODE(ode.eulerStep, p1.func_problem1, x0, .01, 20)
plt.plot(*extract_frames(euler))
plt.title('euler ')
plt.ylabel('trajectory euler')
plt.show()

rungeKutta = ode.solve_ODE(ode.rungeKuttaStep, p1.func_problem1, x0, .01, 20)
plt.plot(*extract_frames(rungeKutta))
plt.title('runge kutta')
plt.ylabel('trajectory rungeKutta')
plt.show()
