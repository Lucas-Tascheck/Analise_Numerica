import numpy as np

#BEST_POLY

'''
Encontre os coeficientes a e b da função taxa de crescimento da saturação y=axx+b que melhor se aproxima da seguinte lista de 12 pontos
(2.106,0.8735)...
'''

#func: 1 / y = 1 / a + b / a * 1 / x

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
    print(f'A = {A}')
    print(f'B = {B}')
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

    x = [0.5303, 0.8829, 2.2698, 3.3011, 3.4365, 4.2884, 5.3503, 6.6073, 6.7482, 8.0028, 8.6439, 9.6663]
    y = [5.9852, 5.5825, 4.7437, 4.2911, 4.2483, 4.2374, 4.0669, 4.052, 4.0064, 4.5265, 4.7709, 5.2772]
    values = [0.9109, 1.1905, 5.5313]

    y_ = []
    for yi in y:
        y_.append(1/yi)
    
    x_ = []
    for xi in x:
        x_.append(1/xi)

    grau = 2

    coefs = best_poly(x, y, grau)

    a0, a1, a2 = best_poly(x, y, grau)

    #a = a0
    #b = a1


    p = build_func(coefs)

    n = len(coefs)

    for xi in range(n):
        print(f'a{xi} = [{coefs[xi]}]')

    #print(f'a = {a} b = {b}')

    n = len(values)
    for xi in range(n):
        print(f'y(x{xi+1}) = {a0 + a1*values[xi] + a2*(values[xi]**2)}')


    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti) for ti in t]

    plt.plot(t, pt)
    plt.savefig('best_poly.png')