#include <stdio.h>
#define ROWS 3
#define COLS 3

void print_matrix(double array[ROWS][COLS]){
    for (int i=0;i<ROWS;i++){
        for(int j=0;j<COLS;j++){
            printf("%.16f\t",array[i][j]);
        }
        printf("\n");
    }
}

void multL(double matriz[ROWS][COLS], int x1, int fim, float mult1){
    double aux[COLS];
    x1-=1;
    fim-=1;
    for(int i=0; i<COLS; i++){
        matriz[fim][i] = mult1 * matriz[x1][i];
    }
}

void somaL(double matriz[ROWS][COLS], int x1, int x2, int fim, float mult1, float mult2){
    double aux[COLS];
    x1-=1;
    x2-=1;
    fim-=1;
    for(int i=0; i<COLS; i++){
        matriz[fim][i]=mult1 * matriz[x1][i] + mult2 * matriz[x2][i];
    }
}

void trocaL(double matriz[ROWS][COLS], int x1, int x2){
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
        {1, -7, 2}, {7, -7, 7}, {-5, 1, 5}  
    };

    //somaL(matriz, linha1, linha2, destino, multiplicador1, multiplicador2)
    //multiplicador1 se aplica em linha1
    //multiplicador2 se aplica em linha2

    //multL(matriz, linha1, destino, multiplicador)
    //multiplica uma unica

    //trocaL(matriz, linha1, linha2)
    //troca linha1 com linha2

    //obs: visto que para nosso amigão C 1/2 = 0, temos q fazer as divisoes em float
    //ex 1.0/2.0, -5.0/2.0...

    //ex func:
    //somaL(E, 3, 2, 2, 1.0/2.0, 1);
    //multL(E, 4, 4, -4.0/5.0);
    //trocaL(E, 2, 4);
    //print_matrix(E);

    somaL(E, 1, 2, 2, -7.0, 1);
    somaL(E, 1, 3, 3, 5.0, 1);
    somaL(E, 2, 3, 3, 17.0/21.0, 1);
    
    print_matrix(E);
}

//quetao 21
//questao 17