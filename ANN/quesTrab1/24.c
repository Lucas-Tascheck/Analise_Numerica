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
    double cons = 1.41 * pow(10, -10);
    double n = 135133502;
    return (n+1)/(1+n*exp(-cons*(n+1)*x)) - n/4;
}


int main(){

    
    double a = 0;
    double b = 1966;
    int n = 12;

    bisection(f,a,b,n);

}