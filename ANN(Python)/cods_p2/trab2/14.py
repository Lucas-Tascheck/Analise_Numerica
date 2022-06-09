import numpy as np

#BEST_POLY

'''
Encontre os coeficientes a e b da função taxa de crescimento da saturação y=axx+b que melhor se aproxima da seguinte lista de 12 pontos
(2.106,0.8735)...
'''

def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p=i+j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, coefs):
    s = coefs[0]
    for i, ci in enumerate(coefs[1:], 1):
        s += ci * x ** i
    return s

def build_func(coefs):
    def temp(x):
        return poly(x, coefs)
    return temp


def modelo(x):
    a, b = -10, 10
    erro = a + (b - a) * np.random.random()
    return 2 + 2.34 * x - 1.86 * x ** 2 - 3.21 * x ** 3 + erro


if __name__ == '__main__':
    

    x = [2.106, 2.6708, 4.6467, 7.3103, 8.874, 9.0225, 10.8809, 12.2423, 14.8024, 16.0894, 18.241, 18.755]
    y = [0.8735, 0.869, 1.2703, 1.5698, 1.6509, 1.7198, 1.7545, 1.8541, 1.9695, 1.9403, 2.0356, 2.0254]
    values = [9.3423, 9.9071, 11.5857]

    y_ = []
    for xi in y:
        y_.append(1/xi)
    
    x_ = []
    for yi in x:
        x_.append(1/yi)

    grau = 1

    coefs = best_poly(x_, y_, grau)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    a = 1/a0
    b = a1 * a


    p = build_func(coefs)

    n = len(coefs)

    for xi in range(n):
        print(f'a{xi} = [{coefs[xi]}]')

    print(f'a = {a} b = {b}')

    n = len(values)
    for xi in range(n):
        print(f'y(x{xi+1}) = {a*(values[xi]/(values[xi] + b))}')


    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti) for ti in t]

    plt.plot(t, pt)
    plt.savefig('best_poly.png')