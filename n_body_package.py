#
import numpy as np

"""
_______my generla formating for the n body problem________
     objlist: a numpy array  of numpy arrays of size 5 where the elements are the n bodies defined
    as follows
    (mass , positon_x, positon_y , velocity_x , velocity_y)
"""


def accel_ij(objI, objJ):  # force on object I from object J divided by the mass of object I (since it gets cancelled
    # anyway)
    massj = objJ[0]  # mass
    posi = np.array([objI[1], objI[2]])  # object I position
    posj = np.array([objJ[1], objJ[2]])  # object J position

    diff = posj - posi  # vector from I to J
    norm = np.linalg.norm(diff)
    accel = massj * diff * (1 / norm ** 3)

    return accel


def accel_Total_i(objlist, i):
    tot = np.zeros(2)

    for j in range(len(objlist)):
        if j != i:
            tot = tot + accel_ij(objlist[i], objlist[j])

    return tot


def n_body_ode(objlist):
    """

    :param objlist: a numpy array  of numpy arrays of size 5 where the elements are the n bodies defined
    as follows
    (mass , positon_x, positon_y , velocity_x , velocity_y)

    :return: the list for each body of (0 ,velocity_x , velocity_y, acceleration_x, acceleration_y):
    """
    derivs = np.zeros((len(objlist), 5))
    for i in range(len(objlist)):
        derivs[i][0] = 0  # mass doesn't ever change
        derivs[i][1] = objlist[i][3]  # x velocity is given in the object's 4th term
        derivs[i][2] = objlist[i][4]  # y velocity is given in the object's 5th term
        derivs[i][3] = accel_Total_i(objlist, i)[0]
        derivs[i][4] = accel_Total_i(objlist, i)[1]
    return derivs
