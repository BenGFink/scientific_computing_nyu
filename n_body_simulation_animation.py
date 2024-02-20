#  N body system Movie Maker
# benjamin fink
#  uses Python 3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import ode_package as ode
import n_body_package as nbp

# initial state of the n_body system
bodySystem = np.array([
    [200, 0, 0, 0, 0],
    [1, 2, 0, 0, 5],
    [1, 3, 0, 0, 8]

])
# the number of bodies in the simulation
N = len(bodySystem)

# calculate the simulation using runge kutta 4th method
simulation = ode.solve_ODE(ode.rungeKuttaStep, nbp.n_body_ode, bodySystem, .005, 10)


def nbody_frame_info(sim):  # converts a simulation into animation appropriate frames
    frameInfo = []
    for t in range(len(sim)):  # the number of frames in the animation
        xs = [item[1] for item in sim[t]]  # extract the list of x positions at time t
        ys = [item[2] for item in sim[t]]  # extract the list of y positions at time t
        frameInfo.append([xs, ys, t])
    return frameInfo


frameInfoList = nbody_frame_info(simulation)
fig, ax = plt.subplots()
ln, = ax.plot([], [], 'ro')
ax.set(aspect=1)
ax.set_title('')
FrameSize = 7
time_text = ax.text(-.9 * FrameSize, .9 * FrameSize, '')
time_text_framework = "time {t:9.2f}"
plt.grid()
plt.title(' 3 body simulation')


def init():
    ax.set_xlim(-FrameSize, FrameSize)
    ax.set_ylim(-FrameSize, FrameSize)
    return ln,


def update(frame):
    xs = frame[0]
    ys = frame[1]
    t = frame[2]
    ln.set_data(xs, ys)
    time_text.set_text(time_text_framework.format(t=t))

    return ln, time_text


ani = FuncAnimation(fig, update, frames=frameInfoList,
                    init_func=init, blit=True, interval=30)

plt.show()

# i have tried alot but i cant manage to make the program save the animation
