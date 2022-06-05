#include <stdio.h>


#define ROWS 3
#define COLS 3

void jacobi(double a[ROWS][COLS], double b[COLS], double chute[COLS], int n){
    double next[COLS];
    for(int k=0;k<n;k++){
        for(int i=0;i<ROWS;i++){
            double bi = b[i];
            for(int j=0;j<COLS;j++){
                if(i!=j){
                    bi-=a[i][j]*chute[j];
                }
            }
            bi/=a[i][i];
            printf("x_%d^(%d) = %.16f\t", i+1, k+1, bi);
            next[i]=bi;
        }
        printf("\n");
        //atualizar chute
        for(int i=0;i<COLS;i++){
            chute[i] = next[i];
        }
    }
}
int main(){

    double m1 = 2.42;
    double m2 = 4.69;
    double m3 = 3.33;
    double g = 9.81;
    double k1 = 84.98;
    double k2 = 79.47;
    double k3 = 92.25;

    double a[ROWS][COLS] = {{(k1+k2), -k2, 0}, {0, (k2 + k3), -k3}, {0, 0, k3}};
    double b[ROWS] =  {m1*g, m2*g, m3*g};

    double chute[ROWS] = {0,0,0};

    int n=18;

    jacobi(a,b,chute,n);

}