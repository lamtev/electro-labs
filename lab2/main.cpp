#include <iostream>
#include <cmath>

int main()
{
    double e     = 2.718282;
    double t_imp = 0.000001;
    double U_imp = 10;
    double T     = 0.000005; // Q = 10, 5 or 3
    double tau   = 0.00001;
    double U_c_t_one   = (0 - U_imp) * pow(e, ( -t_imp / tau)) + U_imp;
    double U_c_t_two   = (U_c_t_one - 0) * pow(e, (-T) / tau) + 0;
    double U_c_t_one_pred = 0;
    double U_c_t_two_pred = 0;

    std::cout << "U_A = " << U_c_t_one << "  " << "U_B = " << U_c_t_two << std::endl;

    while (fabs(U_c_t_one_pred - U_c_t_one) > 10e-5) {

        U_c_t_one_pred = U_c_t_one;
        U_c_t_two_pred = U_c_t_two;

        U_c_t_one   = (U_c_t_two - U_imp) * pow(e, -t_imp / tau) + U_imp;
        U_c_t_two   = (U_c_t_one - 0) * pow(e, (- T) / tau) + 0;

        std::cout << "U_A = " << U_c_t_one << "  " << "U_B = " << U_c_t_two << std::endl;

    }


    return 0;
}