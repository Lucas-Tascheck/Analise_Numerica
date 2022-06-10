import random
import numpy as np
import math

'''
De acordo com o teorema de Taylor, toda função n+1 vezes derivável pode ser aproximada por um polinômio de grau n, 
mais precisamente, se f é n+1 vezes derivável num ponto x0, então para todo x suficientemente próximo de x0, existe um c, entre x e x0, tal que 
'''

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def finite_diffs(xs, ordem, x0, f):
    A = []
    B = []
    n = len(xs)
    for i in range(n):
        A.append([0]*n)
        for j in range(n):
            A[i][j] = xs[j] ** i
        potencias = [k + 1 for k in range(i - ordem, i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial * x0 ** (i - ordem)
        B.append(termo)
    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A,B)
    soma = 0
    for ck, xk in zip(cs, xs):
        soma += ck * f(xk)
    return soma

def taylor(xs, ordens, x0, f, values):
    n = len(ordens)
    for i in range(0, n):
        p = f(x0)
        for k in range(0, n):
            p += (finite_diffs(xs, ordens[k], x0, f) / math.factorial(k+1))*((values[i] - x0)**(k+1))
        erroN = math.sqrt(((f(values[i]) - p)**2))
        print(f'{values[i]} = {p} e |f(x) - p3(x)| = {erroN}')


def f(x):
    return math.log(2 + math.cos(math.exp(-x)))

#Main:

x0 = 0.2855
order = 4
x = [0.078, 0.1206, 0.1664, 0.2348, 0.3436, 0.408, 0.4144, 0.5283]
values = [0.1265, 0.1879, 0.2616, 0.3291]

ordens = []
for i in range(1, order+1):
    ordens.append(i)

taylor(x, ordens, x0, f, values)

num_pontos = 0
a = x0 - 0.25
b = x0 + 0.25
#xs = [a + (b - a) * random.random() for _ in range(num_pontos)]
#xs.sort()

#r = finite_diffs(xs, ordem, x0, f)
#print(xs)
#print(f'aprox para derivada de ordem {ordem} de f no ponto {x0} {r}')