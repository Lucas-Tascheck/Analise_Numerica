#include <stdio.h>
#include<stdlib.h>
#include <math.h>

void false_position(double (*f)(double), double a, double b, double n){
    double fa = f(a);
    double fb = f(b);
    if (fa * fb >= 0){
        printf("O teorema de bolzano nao sabe dizer se existe raiz para f no intervalo [%.16f, %.16f]", a,b);
        return;
    }else{
        double x;
        for (int i=0;i<n;i++){
            x = (a * fb - b * fa) / (fb - fa);
            printf("x_%d = %.16f\n", i+1, x);
            double fx = f(x);
            if (fx==0){
                printf("Encontramos uma raiz para f, x = %.16f",x);
                return;
            }
            if (fa * fx < 0){
                b=x;
                fb=fx;
            }else{
                a=x;
                fa=fx;
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

    double a = 0;
    double b = 10.26;
    int n = 11;

    false_position(f,a,b,n);
}