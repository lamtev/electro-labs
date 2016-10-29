#include <iostream>
#include <cmath>

int main()
{
    double e     = 2.718282;
    double t_imp = 0.000001;
    double U_imp = 10;
    double T     = 0.000005; // Q = 5
    double tau   = 10000 * 10e-9;
    double U_A   = (0 - U_imp) * pow(e, ( -t_imp / tau)) + U_imp;
    double U_B   = (U_A - 0) * pow(e, -( T - t_imp) / tau) + 0;
    double U_A_pred = 0;
    double U_B_pred = 0;

    while (fabs(U_A_pred - U_A) > 10e-9) {

       U_A_pred = U_A;
       U_B_pred = U_B;

       U_B   = (U_A - 0) * pow(e, - (T - t_imp) / tau) + 0;
       U_A   = (U_B - U_imp) * pow(e, -t_imp / tau) + U_imp;

    }

    std::cout << "U_A = " << U_A << std::endl;
    std::cout << "U_B = " << U_B << std::endl;

    return 0;
}
