from tokenize import PlainToken
import numpy as np
import math as m

def lagrange(x,y):
    #retorn yi dividido pelo denominador do polinomio li
    num = len(x)
    coefs = []
    for i in range(num):
        prod = 1
        for j in range(num):
            if i != j:
                prod *= (x[i] - x[j])
        ci = y[i] / prod
        coefs.append(ci)
    print(coefs)
    return coefs

def pl(t: float, x: list[float], coefs: list[float])->float:
    soma = 0
    num=len(coefs)
    for i in range(num):
        prod = 1
        for j in range(num):
            if i != j:
                prod *= (t - x[j])
        prod *= coefs[i]
        soma += prod
    return soma


def poly(x, coefs):
    def func(t):
        return pl(t, x, coefs)
    return func

if __name__ == '__main__':

    def p2(x):
        return 1/(1+25*(x**2))

    def p3(x):
        return m.cos(m.sin(m.log(x**2)))

    #exemplo
    x = [-0.454, 0.163, 0.624]
    y = [p2(-0.454), p2(0.163), p2(0.624)]



    c = lagrange(x,y)
    lagr = poly(x, c)
    print(m.sqrt((p2(0.53) - lagr(0.53))**2))



#visualização

import matplotlib.pyplot as plt
plt.scatter(x, y)

t = np.linspace(min(x), max(x), 100)
lt = [lagr(ti) for ti in t]

plt.plot(t, lt)

plt.savefig('lagrange.png')
