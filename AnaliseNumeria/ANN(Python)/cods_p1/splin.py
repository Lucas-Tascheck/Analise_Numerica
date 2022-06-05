# Spline method

import numpy as np
import matplotlib.pyplot as plt
import math as m


def spline(x, y):
    """
    """
    n = len(x)
    a = {k: v for k, v in enumerate(y)}
    h = {k: x[k+1] - x[k] for k in  range(n - 1)}

    A = [[1] + [0] *(n -1)]
    for i in range(1, n-1):
        row = [0]* n
        row[i-1] = h[i-1]
        row[i] =  2*(h[i-1] + h[i])
        row[i+1] = h[i]
        A.append(row)
    A.append([0]*(n-1)+[1])

    B = [0]
    for k in range(1, n - 1):
        row = 3*(a[k+1] - a[k]) / h[k] - 3 * (a[k] - a[k-1])/h[k-1]
        B.append(row)
    B.append(0)

    c = dict(zip(range(n), np.linalg.solve(A,B)))
    # print('Valores dos c\'s ')

    b = {}
    d = {}
    for k in range(n-1):
        b[k] = (1/h[k]) * (a[k+1] - a[k]) - (h[k]/3) * (2*c[k]+c[k+1])
        d[k] = (c[k+1] - c[k])/(3*h[k])

    s = {}
    for k in range(n-1):
        eq = f'{a[k]}{b[k]:+}*(x-{x[k]}){c[k]:+}*(x-{x[k]})**2{d[k]:+}*(x-{x[k]})**3'
        eq2 = a[k]+b[k]*(ponto-x[k])+c[k]*(ponto-x[k])**2+d[k]*(ponto-x[k])**3
        s2[k] = {'eq': eq2, 'domain':[x[k], x[k+1]]} 
        s[k] = {'eq': eq, 'domain':[x[k], x[k+1]]}
    return s

def q(x):
    return m.sin(m.sqrt(m.pi+(x**2)))

def q2(x):
    return m.cos(m.sin(m.log(x**2)))

s2 = {}
ponto = -1.049

x = [0.736, 1.13, 2.203, 2.906]
y = [q2(0.736), q2(1.13), q2(2.203), q2(2.906)]

eqs = spline(x,y)
eqs2 = s2

eq0 = eqs

cont = len(eq0)
for xi in range(cont):
    print(f'{xi} = {eq0[xi]}')
    print('')

for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label= f"$S_{key}(x)$")

plt.scatter(x,y)
plt.legend()
plt.savefig('spline.png')


# tem erro no np.linalg.solve(A, B)
# mas nao sei arrumar
# entao vai assim msm