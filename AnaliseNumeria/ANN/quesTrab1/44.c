#include <stdio.h>
#include <math.h>

#define ROWS 6
#define COLS 7

void print_matrix(double array[ROWS][COLS]){
    for (int i=0;i<ROWS;i++){
        for(int j=0;j<COLS;j++){
            printf("%f\t",array[i][j]);
        }
        printf("\n");
    }
}

void gauss(double E[ROWS][COLS]){
    for (int j=0;j<COLS-2;j++){
        for(int i=j;j<ROWS;i++){
            if(E[i][j] != 0){
                if (i!=j){
                    //é preciso trocar linhas
                    for(int k=0;k<COLS;k++){
                        double temp = E[i][k];
                        E[i][k] = E[j][k];
                        E[j][k] = temp;
                    }
                }
                //aplicar operações elementares em linha
                //a * Lj + Lm -> Lm
                for (int m=j+1;m<ROWS;m++){
                    double a = -E[m][j] / E[j][j];
                    for(int n = j; n<COLS;n++){
                        E[m][n] += a * E[j][n];
                    }
                }
                print_matrix(E);
                printf("\n");
                break;
            }
        }
    }
}

void reverse_substitution(double E[ROWS][COLS]){
    double answer[ROWS];
    for (int i=0;i<ROWS;i++){
        int d = ROWS - 1 - i;
        double b = E[d][COLS - 1]; // termo independente
        for(int j=d+1;j<COLS-1;j++){
            b-= E[d][j] * answer[j];
        }
        double xd = b / E[d][d];
        answer[d] = xd;
         printf("x_%d = %.16f\n", i+1,xd);
    }
}


int main(){

    double f1 = 827;
    double f2 = 1290;
    double f3 = 1091;

    double teta1 = 55;
    double teta2 = 75;
    double teta3 = 60;


    double alfa = 52;
    double beta = 51;

    double sina = sin((alfa*M_PI)/180);
    double sinb = sin((beta*M_PI)/180);

    double cosa = cos((alfa*M_PI)/180);
    double cosb = cos((beta*M_PI)/180);


    double E[ROWS][COLS] =  {{cosa, 0, -cosb, 0, 0, 0, -f1*cos((teta1*M_PI)/180)}, {sina, 0, sinb, 0, 0, 0, -f1*sin((teta1*M_PI)/180)}, {-cosa, -1, 0, -1, 0, 0, f2*cos((teta2*M_PI)/180)}, {-sina, 0, 0, 0, -1, 0, -f2*sin((teta2*M_PI)/180)}, {0, 1, cosb, 0, 0, 0, -f3*cos((teta3*M_PI)/180)}, {0, 0, -sinb, 0, 0, -1, -f3*sin((teta3*M_PI)/180)}};

    print_matrix(E);
    printf("\n");
    gauss(E);
    reverse_substitution(E);
    
}