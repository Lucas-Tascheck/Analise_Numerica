#include <stdio.h>
#include <math.h>

#define ordemEerro 12
// 4 pois a primeira coluna deve ter 'error_order / 2' elementos
#define numElemsFirstCol 6

double trapz(double (*f)(double), double a, double b, int n){
    double soma = 0;
    double h = (double)(b - a) / (double)n;
    for(int i = 1; i < n; i++){
        double xi = a + i * h;
        soma += f(xi);
    }
    soma *= 2;
    soma += f(a);
    soma += f(b);
    soma *= (0.5 * h);
    return soma;
}


void romberg(double array[], int error_order){

    int numCols = error_order / 2 - 1;
    for(int i = 0; i < numCols; i++){
        for(int j = 0; j < numCols; j++){
            double numer = pow(2, (i + 1) * 2) * array[j + 1] - array[j];
            double denom = pow(2, (i + 1) * 2) - 1;
            array[j] = numer / denom;
        }
    }
    printf("Aprox O(h^%d) = %.16f\n", error_order, array[0]);
}


double f(double x){
    return exp(-x*x);
}

int main(){

    //exemplo
    //aprox a integral de exp(-x*x), de 0 a 1

    double a = 0;
    double b = 1;
    double h = 0.25;
    int n = (int)((b - a) / h);


    printf("%.16f\n", (double)n);

    double coluna_F1[numElemsFirstCol] = {};
    for(int i = 0; i < numElemsFirstCol; i++){
        coluna_F1[i] = trapz(f, a, b, (i + 1) * n);
    }
    romberg(coluna_F1, ordemEerro);

}