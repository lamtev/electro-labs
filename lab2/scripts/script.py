import math


def print_u():
    global i
    print("{0}) U_C(0) = {1:.3f}, U_C(t_imp) = {2:.3f}".format(i, U_c_0, U_c_t_imp))
    i += 1


i = 1
Q = 5 * 10E-7  # 10, 5 or 3
t_imp = 10E-7
U_imp = 10

tau = 10E-6
U_c_t_imp = (0 - U_imp) * math.e ** (-t_imp / tau) + U_imp
U_c_0 = (U_c_t_imp - 0) * math.e ** (-(Q - t_imp) / tau)
U_c_t_imp_before = 0
U_c_0_before = 0

print_u()
while math.fabs(U_c_t_imp_before - U_c_t_imp) > 10E-5:
    U_c_t_imp_before = U_c_t_imp
    U_c_t_imp = (U_c_0 - U_imp) * math.e ** (-t_imp / tau) + U_imp
    U_c_0 = (U_c_t_imp - 0) * math.e ** (-(Q - t_imp) / tau)
    print_u()
