#include <stdio.h>
#include <math.h>

#define ROWS 3
#define COLS 4

void print_matrix(double array[ROWS][COLS]){
    for (int i=0;i<ROWS;i++){
        for(int j=0;j<COLS;j++){
            printf("%f\t",array[i][j]);
        }
        printf("\n");
    }
}

int gauss(double E[ROWS][COLS]){
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

    double m1 = 144;
    double m2 = 100;
    double m3 = 81;

    double g  = 9.81;

    double u1 = 0.11;
    double u2 = 0.17;
    double u3 = 0.47;

    double alfa = 45;

    double px1 =  m1*g*sin((alfa*M_PI)/180);
    double px2 =  m2*g*sin((alfa*M_PI)/180);
    double px3 =  m3*g*sin((alfa*M_PI)/180);

    double u1fn = u1*(m1*g*cos((alfa*M_PI)/180));
    double u2fn = u2*(m2*g*cos((alfa*M_PI)/180));
    double u3fn = u3*(m3*g*cos((alfa*M_PI)/180));

    double E[ROWS][COLS] =  {{m1, 1, 0, px1-u1fn}, {m2, -1, 1, px2-u2fn}, {m3, 0, -1, px3-u3fn}};

    print_matrix(E);
    printf("\n");
    gauss(E);
    reverse_substitution(E);
    
}