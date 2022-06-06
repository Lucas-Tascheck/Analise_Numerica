import numpy as np
import math as m

#exemplos
def p2(x):
    return m.exp(m.cos(x)**2)+m.exp(-x**2) + m.log(x)

#exemplo
x = [2.026, 3.009, 3.756, 4.387, 4.787]
y = [1.869, 3.998, 3.811, 3.137, 1.409]

def poly(x, y):
    n = len(x) - 1
    a = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi ** j)
        a.append(row)
    return np.linalg.solve(a, y)


def func_poly(x, coeffs):
    first = coeffs[0]
    return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:], 1)])



if __name__== '__main__':
    coeffs = poly(x, y)
    num2 = len(coeffs)

    valorX = 3.711

    for xi in range(num2):
        print(f'a{xi} [{coeffs[xi]:.16f}]')

    result = coeffs[0]
    for i in range(1, num2):
        result += coeffs[i]*(valorX**i)
    print(result)



    def p(x):
        return func_poly(x, coeffs)

    #visualizacao
    import matplotlib.pylab as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 100)
    pt = [p(ti) for ti in t]
    st = np.sin(t)

    plt.plot(t, pt)
    plt.plot(t, st)

    plt.savefig('interp.png')

