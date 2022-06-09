import random
import numpy as np
import math

'''
De acordo com o teorema de Taylor, toda função n+1 vezes derivável pode ser aproximada por um polinômio de grau n, mais precisamente, 
se f é n+1 vezes derivável num ponto x0, então para todo x suficientemente próximo de x0, existe um c, entre x e x0, tal que 
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

def f(x):
    return math.log(2 + math.cos(math.exp(-x)))

x0 = 0.2855
ordem = 4
xs = [0.078, 0.1206, 0.1664, 0.2348, 0.3436, 0.408, 0.4144, 0.5283]
values = [0.1265, 0.1879, 0.2616, 0.3291]

ordem1 = 1
ordem2 = 2
ordem3 = 3

p = 0
n = len(values)
for i in range(n):
    p = f(x0) + finite_diffs(xs, ordem1, x0, f)*(values[i] - x0) + ((finite_diffs(xs, ordem2, x0, f)/2) * ((values[i]-x0)**2)) + ((finite_diffs(xs, ordem3, x0, f)/6) * ((values[i]-x0)**3)) + ((finite_diffs(xs, ordem, x0, f)/24) * ((values[i]-x0)**4))
    erroN = math.sqrt(((f(values[i]) - p)**2))
    print(f'{values[i]} = {p} e |f(x) - p3(x)| = {erroN}')

num_pontos = 0
a = x0 - 0.25
b = x0 + 0.25
#xs = [a + (b - a) * random.random() for _ in range(num_pontos)]
#xs.sort()

#r = finite_diffs(xs, ordem, x0, f)
#print(xs)
#print(f'aprox para derivada de ordem {ordem} de f no ponto {x0} {r}')