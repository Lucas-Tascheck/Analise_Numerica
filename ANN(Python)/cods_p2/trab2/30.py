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
    return x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)

#Main:

x0 = 0.751
x = [0.5398, 0.5933, 0.6142, 0.6887, 0.7159, 0.7769, 0.811, 0.8784, 0.9293, 0.9653]
values = [0.5827, 0.6043, 0.6053, 0.7018, 0.9361]
order = 5

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