import numpy as np
import math


def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def finite_diffs(x, ordem, x0, f):
    A = []
    B = []
    n = len(x)
    for i in range(n):
        A.append([0] * (n))
        for j in range(n):
            A[i][j] = x[j] ** i
        potencias = [k + 1 for k in range(i - ordem, i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial * x0 ** (i - ordem)
        B.append(termo)
    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A, B)
    soma = 0
    for ck, xk in zip(cs, x):
        soma += ck * f(xk)
    return soma

if __name__ == '__main__':

    def f(x):
        return math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x)

    ordem = 4
    x0 = 5.2826
    x = [5.0897, 5.1351, 5.1938, 5.2495, 5.3094, 5.3753, 5.4262, 5.5011]

    #num_pontos = 8
    #a = x0 - 0.2
    #b = x0 + 0.2
    #x = [a + (b - a ) * random.random() for _ in range(num_pontos)]
    #xs.sort()

    r = finite_diffs(x, ordem, x0, f)

    print(f'aproximação para derivada de {ordem} de f no ponto {x0} é: ', r)