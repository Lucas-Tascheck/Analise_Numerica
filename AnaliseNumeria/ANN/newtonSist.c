#include <stdio.h>


double g1(double x, double y){
    return x*x+y*y-5;
}

double g2(double x, double y){
    return x*x+x*y*y*y-3;
}

double g1x(double x, double y){
    return 2*x;
}

double g1y(double x, double y){
    return 2*y;
}

double g2x(double x, double y){
    return 2*x+y*y*y;
}

double g2y(double x, double y){
    return 3*x*y*y;
}

double det(double x, double y){
    //retorna o det de
    //[g1x, g1y]
    //[g2x, g2y]
    return g1x(x, y)*g2y(x,y)-g1y(x,y)*g2x(x,y);
}

void newton(double x, double y, int n){
    for(int k = 0; k<n; k++){
        double xk = x-(g2y(x, y) * g1(x, y)-g1y(x,y)*g2(x,y))/det(x,y);
        double yk = y-(-g2x(x, y) * g1(x, y)+g1x(x,y)*g2(x,y))/det(x,y);
        printf("x^(%d) = %.16f\n", k+1, xk);
        printf("y^(%d) = %.16f\n\n", k+1, yk);
        x = xk;
        y = yk;
    }
}


int main(){

    double x0 = -0.1132;
    double y0 = -2.4486;
    int n = 4;

    newton(x0, y0, n);
}