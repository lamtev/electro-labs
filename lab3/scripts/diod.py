# Assisted by YURIJ LEZHENIN

from math import exp, log
import numpy as np
from scipy.optimize import fsolve

phi = 0.025875  # const
path = '../data/'  # path to data files


def fun(x):  # Ebers-Moll equation
    i_0, m = x
    u1, i1 = 0.53, 0.029  # point 1
    u2, i2 = 0.73, 0.269  # point 2
    return i_0 * (exp(u1 / (m * phi)) - 1) - i1, \
           i_0 * (exp(u2 / (m * phi)) - 1) - i2


i_0, m = fsolve(fun, [10, 10])
print(i_0, m)


def em_i(u):
    return i_0 * (exp(u / (m * phi)) - 1)


def em_u(i):
    return log((i / i_0 + 1), exp(1)) * (m * phi)


f = open(path + 'vac_theory.csv', 'w')
f.write('u,i\n')
for u in np.arange(0.43, 0.77, 0.03):
    f.write(str(u) + ',' + str(em_i(u) * 1000) + '\n')

f = open(path + 'half_wave_theory.csv', 'w')
f.write('i,u_n,u_p\n')
for i in np.arange(0.01, 0.3, 0.02):
    u = 6.3 * 1.41 - em_u(i) - 1 * i  # U2 = 6.3
    f.write(str(i * 1000) + ',' + str(u) + ',' + str(i * 1000 * 0.02 / 1.5) + '\n')

f = open(path + 'full_wave_theory.csv', 'w')
f.write('i,u_n,u_p\n')
for i in np.arange(0.01, 0.3, 0.02):
    u = 6.3 * 1.41 - em_u(i) - 2 * i  # U2 = 6.3
    f.write(str(i * 1000) + ',' + str(u) + ',' + str(i * 1000 * 0.01 / 1.5) + '\n')