#include <stdio.h>

void fixed_point(double (*f)(double), double x0, int n){
    for (int i=0;i<n;i++){
        double xn = f(x0);
        printf("x_%d = %.16f\n", i+1,xn);
        x0 = xn;
    }
}

double ex1(double x){
        return x / 2.0 + 1 / x;
}

int main() {

    double x0 = 1.678;
    int n=5;
    fixed_point(ex1, x0, n);

}