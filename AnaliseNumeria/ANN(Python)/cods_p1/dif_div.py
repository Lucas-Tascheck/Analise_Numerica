

def dif_div(x, y):
    num = len(x)
    Y = [yi for yi in y]
    coefs = [y[0]]
    for j in range(num-1):
        for i in range(num-1-j):
            numer = Y[i+1] - Y[i]
            denom = x[i+1+j] - x[i]
            div = numer / denom
            Y[i] = div
        coefs.append(Y[0])
    return coefs

def poly(t, x, coefs):
    val = 0
    num = len(coefs)
    for i in range(num):
        prod = 1
        for j in range(i):
            prod *= (t - x[j])
        val += coefs[i] * prod
    return val

def build_func(x, coefs):
    def temp(t):
        return poly(t, x, coefs)
    return temp


if __name__ == '__main__':

    import math as m

    def p2(x):
        return m.cos(x)**3 + 2*(m.cos(x)**2) + 1

    def p3(x):
        return m.cos(m.sin(m.log(x**2)))

    #exemplo
    x = [0.798, 1.434, 2.798]
    y = [p3(0.798), p3(1.434), p3(2.798)]

    coefs = dif_div(x, y)
    p = build_func(x, coefs)

    print(coefs)
    print(p(1), p(2), p(3), p(4))

    #view
    import matplotlib.pyplot as plt
    import numpy as np
    t = np.linspace(min(x), max(x), 100)
    pt = [p(ti) for ti in t]

    plt.scatter(x, y)
    plt.plot(t, pt)

    plt.savefig('Dif_div.png')