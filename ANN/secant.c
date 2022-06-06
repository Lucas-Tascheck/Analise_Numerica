#include <stdio.h>
#include <math.h>

void secant(double(*f)(double), double x0, double x1, int n){
    double fx0 = f(x0);
    double fx1 = f(x1);
    if(fx0 == fx1){
        printf("Escolha outras estimativas iniciais");
    }
    else{
        for(int i = 0; i<n; i++){
            double x2 = (x0 * fx1 - x1 * fx0)/(fx1-fx0);

            fx0 = fx1;
            fx1 = f(x2);

            if(fx0 == fx1){
                printf("x_%d = %.16f (precisei parar)\n", i+2, x2);
            }
            else{
                printf("x_%d = %.16f\n", i+2, x2);
                x0 = x1;
                x1 = x2;
            }
        }
    }
}


double f(double x){
    double r = 5.13;
    double v = 326.35;

    return ((M_PI*x*x)*(3*r-x))/3 - v;
}

int main(){

    double x0 = 0.82;
    double x1 = 9.59;
    int n=5;

    secant(f,x0,x1,n);


}