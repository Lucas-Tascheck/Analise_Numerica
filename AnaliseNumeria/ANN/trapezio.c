#include<stdio.h>
#include<math.h>

void trapz(double(*f)(double), double a, double b, int n){
    double soma = 0;
    double h = (double)(b - a) / (double)n;
    for (int k = 1; k < n; k++){
        soma += f(a + k * h);
    }
    soma *= 2;
    soma += f(a);
    soma += f(b);
    soma *= (h/2.0);
    printf("Area aproximadamente: %.16f\n", soma);
}


double func1(double x){
    return exp(-x*x);
}


double func2(double x){
    return cos(x*x);
}

double func3(double x){
    return exp(-x*x);
}


int main(){

//exemplo 1
double a = -1;
double b = 1;
int n = 1000000; // num de intervalo

trapz(func2, a, b, n);

}