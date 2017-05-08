from math import sqrt, pi

f = open('../data/f0_as_f_of_R_theory.csv', 'w', encoding='utf-8-sig')

r3 = 33000
c1 = 10 ** (-9)
c2 = 2 * 10 ** (-9)

f.write('r,f0\n')

for i in range(2, 121):
    r1 = i * 1000
    s = str(i) + ',' + str(sqrt(1 / r1 * 1 / r3 / c1 / c2) / 2 / pi / 1000)
    f.write(s + '\n')

f.close()
