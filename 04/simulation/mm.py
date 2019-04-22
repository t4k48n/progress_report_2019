import numpy as np
from numpy import cos, sin, sqrt

import scipy.stats as sst

import matplotlib.pyplot as plt

l1 = 1.0
l2 = 1.0

#dl1 = 0.02
#dl2 = 0.02
dl1 = 1.0 * np.pi / 180.0
dl2 = 1.0 * np.pi / 180.0

def M(q1, q2, z1, z2):
    return sqrt(np.abs((l2**2*sin(dl1*z1 + dl2*z2 + q1 + q2)**2 + (-l1*sin(dl1*z1 + q1) - l2*sin(dl1*z1 + dl2*z2 + q1 + q2))**2)*(l2**2*cos(dl1*z1 + dl2*z2 + q1 + q2)**2 + (l1*cos(dl1*z1 + q1) + l2*cos(dl1*z1 + dl2*z2 + q1 + q2))**2) - (-l2**2*sin(dl1*z1 + dl2*z2 + q1 + q2)*cos(dl1*z1 + dl2*z2 + q1 + q2) + (-l1*sin(dl1*z1 + q1) - l2*sin(dl1*z1 + dl2*z2 + q1 + q2))*(l1*cos(dl1*z1 + q1) + l2*cos(dl1*z1 + dl2*z2 + q1 + q2)))**2))

p_norm = lambda z: sst.norm.pdf(z, loc=0, scale=1)
a_norm = -np.infty
b_norm = np.infty

p = p_norm
a = a_norm
b = b_norm

def Me(q1, q2):
    from scipy.integrate import dblquad
    m = lambda z1, z2: M(q1, q2, z1, z2) * p(z1) * p(z2)
    result = dblquad(m, a, b, lambda _: -1.0, lambda _: 1.0)
    Me.latest_error = result[1]
    return result[0]
Me.latest_error = np.nan

def Mv(q1, q2):
    from scipy.integrate import dblquad
    me = Me(q1, q2)
    v = lambda z1, z2: (M(q1, q2, z1, z2) - me)**2.0 * p(z1) * p(z2)
    result = dblquad(v, a, b, lambda _: -1.0, lambda _: 1.0)
    Mv.latest_error = result[1]
    return result[0]
Mv.latest_error = np.nan

qs = np.linspace(0.0, 360.0, 73)
me = np.vectorize(Me)(0.0, qs * np.pi / 180.0)
mv = np.vectorize(Mv)(0.0, qs * np.pi / 180.0)
ms = np.sqrt(mv)
se_ratio = ms / me

plt.figure("me")
plt.plot(qs, me)

plt.figure("mv")
plt.plot(qs, mv)

plt.figure("se_ratio")
plt.plot(qs, se_ratio)

plt.show()
