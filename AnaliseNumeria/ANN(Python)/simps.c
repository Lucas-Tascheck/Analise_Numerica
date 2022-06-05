#include<stdio.h>
#include<math.h>

void simps(double(*f)(double), double a, double b, int n){
    if (n %  2 != 0){
        printf("O numero de intervalos deve ser par!");
        return;
    }
    double soma = 0;
    int numParabolas = n / 2;
    double h = (double)(b - a) / (double)n;
    for(int k = 0; k < numParabolas; k++){
        double x0 = a + (2 * k) * h;
        double x1 = a + (2 * k + 1) * h;
        double x2 = a + (2 * k + 2) * h;
        soma += (f(x0) + 4 * f(x1) + f(x2));
    }
    soma *= (h / 3.0);
    printf("Area aprox: %.16f\n", soma);
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
double a = 0;
double b = 1;
int n = 100; // num de intervalo

simps(func1, a, b, n);

}