#include <stdio.h>
#include <math.h>

void newton(double(*f)(double), double(*df)(double), double x0, int n){
    double der = df(x0);
    if(der==0){
        printf("Escolha outra estimativa");
    }
    else{
        for (int i=0;i<n;i++){
        double x1 = x0 - f(x0) / der;
        der = df(x1);
        if(der==0){
            printf("x_%d = %.16f (precisei parar)\n", i+1, x1);
        }
        else{
            printf("x_%d = %.16f\n", i+1, x1);
        }
        x0=x1;
        }
    }
}

double f(double x){
    double g = 9.81;
    double c = 26.79;
    double v = 35.95;
    double t = 7.26;

    return ((g*x)*(1-exp(-(c/x)*t)))/c - v;
    }

double df(double x){
        return (327*(5000*exp(972477/(5000*x))*x - 5000*x - 972477))/(4465000*exp(972477/(5000*x))*x);
    }

int main(){

    double x0 = 28.04;
    int n = 5;

    newton(f,df,x0,n);


}