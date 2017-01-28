#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdlib>

void print(double U_c_0, double U_c_t_imp);

int main(int argc, char **argv) {
    double T = 0.000005; // Q = 10, 05 or 03
    double e     = 2.718282;
    double t_imp = 0.000001;
    double U_imp = 10;

    double tau   = 0.00001;
    double U_c_t_imp   = (0 - U_imp) * pow(e, ( -t_imp / tau)) + U_imp;
    double U_c_0   = (U_c_t_imp - 0) * pow(e, -(T - t_imp) / tau) + 0;
    double U_c_t_imp_before = 0;
    double U_c_0_before = 0;

    print(U_c_0, U_c_t_imp);

    while (fabs(U_c_t_imp_before - U_c_t_imp) > 10e-5) {

        U_c_t_imp_before = U_c_t_imp;
        U_c_0_before = U_c_0;

        U_c_t_imp   = (U_c_0 - U_imp) * pow(e, -t_imp / tau) + U_imp;
        U_c_0   = (U_c_t_imp - 0) * pow(e, -(T - t_imp) / tau) + 0;

        print(U_c_0, U_c_t_imp);

    }

    return 0;
}

void print(double U_c_0, double U_c_t_imp) {
    std::cout << "U_C(0) = " << U_c_0 << "  " << "U_C(t_imp) = " << U_c_t_imp << std::endl;
}}