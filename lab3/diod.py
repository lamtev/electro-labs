# COPYRIGHT by YURIJ LEZHENIN

from math import exp, log
import numpy as np
import scipy.optimize


def function(p):
    x, y = p
    return x * (exp(0.53 / (y * 0.025875)) - 1) - 0.029, x * (exp(0.73 / (y * 0.025875)) - 1) - 0.269
    # Точка 1: {0.53, 0.029}, Точка 2: {0.73, 0.269}
    # 0.25875 = const


i_0, m = scipy.optimize.fsolve(function, [10, 10])
print(i_0, m)


def shokli_i(u):
    return i_0 * (exp(u / (m * 0.025875)) - 1)


def shokli_u(i):
    return log((i / i_0 + 1), exp(1)) * (m * 0.025875)


f = open('d_vac.csv', 'w')
f.write('u, i \n')
for u in np.arange(0.3, 0.75, 0.03):
    f.write(str(u) + ', ' + str(shokli_i(u) * 1000) + '\n')

f = open('theo_u(i)_1.csv', 'w')
f.write('i, u \n')
for i in np.arange(0.01, 0.3, 0.02):
    # U2 = 6.3
    u = 6.3 * 1.41 - shokli_u(i) - 1 * i
    f.write(str(i * 1000) + ', ' + str(u) + '\n')

f = open('theo_u(i)_2.csv', 'w')
f.write('i, u \n')
for i in np.arange(0.01, 0.3, 0.02):
    # U2 = 6.3
    u = 6.3 * 1.41 - shokli_u(i) - 2 * i
    f.write(str(i * 1000) + ', ' + str(u) + '\n')
