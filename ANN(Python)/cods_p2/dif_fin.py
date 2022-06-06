import numpy as np
import math

#CODIGO DO PROFESSOR INCOMPLETO!!!!!!!!!!

def coeffs_dif_fin(x0, x, k):
    n = len(x)
    A, B = [[1] * n], [0]

    for i in range(1, n):
        row_i = [xi ** i for xi in x]
        A.append(row_i)
        if i < k:
            B.append(0)
        elif i == k:
            B.append(math.factorial(k))
        else:
            numer = math.factorial(i)
            denom = math.factorial(i - k)
            el = (numer/denom) * x0 ** (i - k)
            B.append(el)
    return np.linalg.solve(A, B)

def dif_fin(coeffs, y):
    return sum(ci * yi for ci, yi in zip(coeffs, y))


if __name__ == '__main__':
    #exemplo 1
    def f(x):
        return math.exp(-x**2)+math.cos(x)+3

    x0 = 2.9242
    x = [2.7063, 2.7094, 2.7581, 2.7756, 2.8159, 2.8707, 2.903, 2.9266, 2.9706, 2.9936, 3.0243, 3.069, 3.0874, 3.1126, 3.1472]

    y = [f(xi) for xi in x]

    ordem = 5
    #n = 16
    #e = 0.1

    coeffs = coeffs_dif_fin(x0, x, ordem)
    aprox = dif_fin(coeffs, y)
    print(f'{coeffs = }')
    print(f'{aprox = }')
