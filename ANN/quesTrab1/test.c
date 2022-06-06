#include <stdio.h>
#define ROWS 4
#define COLS 3

void print_matrix(double array[ROWS][COLS]){
    for (int i=0;i<ROWS;i++){
        for(int j=0;j<COLS;j++){
            printf("%.16f\t",array[i][j]);
        }
        printf("\n");
    }
}

void somaL(int x1, int x2, int fim, double matriz[ROWS][COLS], double mult1, double mult2){
    double aux[COLS];
    x1-=1;
    x2-=1;
    fim-=1;
    if(mult2==0){
        for(int i=0; i<COLS; i++){
        aux[i]=mult1 * matriz[x1][i];
        }
        for(int i=0; i<COLS; i++){
            matriz[fim][i]=aux[i];
        }
        return;
    }
    for(int i=0; i<COLS; i++){
        aux[i]=mult1 * matriz[x1][i] + mult2 * matriz[x2][i];
    }
    for(int i=0; i<COLS; i++){
        matriz[fim][i]=aux[i];
    }
}

void trocaL(int x1, int x2, double matriz[ROWS][COLS]){
    x1-=1;
    x2-=1;
    double aux;
    for(int i=0; i<COLS; i++){
        aux = matriz[x1][i];
        matriz[x1][i]=matriz[x2][i];
        matriz[x2][i]=aux;
    }
}

int main(){

double E[ROWS][COLS] = {
        {3,-0.75,3}, {-3,1.5,-1}, {1.75,-3,-0.2}, {-0.1111111111111111,0.7142857142857143,-0.8333333333333333}   
    };

    somaL(3, 2, 2, E, 0.5, 1);
    somaL(4, 0, 4, E, -0.8, 0);
    somaL(1, 0, 1, E, 0.125, 0);
    trocaL(2, 4, E);
    trocaL(1, 3, E);
    somaL(4, 1, 1, E, 1.6, 1);
    print_matrix(E);
}

//quetao 21
//questao 17