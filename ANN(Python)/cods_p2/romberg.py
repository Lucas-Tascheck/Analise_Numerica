import math

#define ordemEerro 4
# 4 pois a primeira coluna deve ter 'error_order / 2' elementos
#define numElemsFirstCol 2

def trapz(f, a, b, n):
    soma = 0
    h = (b - a) / n
    for i in range(1, n):
        soma += f(a + i * h)
    
    soma *= 2
    soma += f(a)
    soma += f(b)
    soma *= (0.5 * h)
    return soma



def romberg(array, error_order):

    numCols = error_order // 2 - 1
    for i in range(numCols - 1):
        for j in range(numCols - 1):
            numer = 2**((i + 1) * 2) * array[j + 1] - array[j]
            denom = 2**((i + 1) * 2) - 1
            array[j] = numer / denom
    print(f'Aprox O(h^{error_order}) = {array[0]}')


def f(x):
  g = 9.81
  m = 65.73
  cd = 0.48
  return math.sqrt((g*m) / cd)*math.tanh(math.sqrt((g*cd) / m) * x)

def f2(x):
    return math.sqrt(1+x**2)

def f3(x):
    return math.cos(-x**2/3)

def f4(x):
    return (x+1/x)**2

def f5(x):
    return math.exp(-x**2)



if __name__ == '__main__':
    #exemplo
    #aprox a integral de exp(-x*x), de 0 a 1


  
    a = [0]
    b = [7.71]
    order = [8]
    h = [7.71/10]


    tam = len(a)
    for k in range(tam):
        coluna_F1 = []
        numElemsFirstCol = order[k] // 2
        n = (int)((b[k] - a[k]) // h[k])
        for i in range(numElemsFirstCol):
            coluna_F1.append(trapz(f, a[k], b[k], 2**i * n))
        romberg(coluna_F1, order[k])