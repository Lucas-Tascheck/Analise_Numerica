#include <stdio.h>
#include <math.h>

void bisection(double(*f)(double), double a, double b, int n){
    if (f(a) * f(b) >= 0){
        printf("O teorema de Volzano nao sabe dizer se existe raiz no intervalo [%.f,%.f]",a,b);
        return;
    }else{
        for(int i=0;i<n;i++){
            double m = 0.5*(a+b);
            printf("x_%d = %.16f\n", i+1, m);
            if (f(m) == 0){
                printf("Yay vc encontrou uma raiz para r = %.16f", m);
            }
            else{
                if (f(a) * f(m) < 0){
                    b = m;
                } else{
                    a = m;
                }
            }
        }
    }
}

double f(double x){
    double g = 9.81;
    double v = 7.24;
    double t = 9.02;
    double L = 6.8;

    return sqrt(2*g*x)*tanh((sqrt(2*g*x)*t)/(2*L)) - v;
}


int main(){

    
    double a = 0.03;
    double b = 16.74;
    int n = 12;

    bisection(f,a,b,n);

}