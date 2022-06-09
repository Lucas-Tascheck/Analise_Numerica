import numpy as np

#BEST_POLY

'''
Um pesquisador relatou os dados tabulados a seguir de um experimento realizado para determinar a taxa de crescimento k (por dia)
de bactérias como uma função da concentração de oxigênio c (em mg/L).
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
    

    x = [1.1879, 2.8244, 2.9356, 4.6377, 5.3966, 5.6821, 6.5251, 7.7879, 9.2358, 10.1294, 10.3599, 11.5123]
    y = [0.534, 1.7992, 1.9232, 2.7225, 2.9678, 2.9819, 3.0258, 3.317, 3.4167, 3.5039, 3.5791, 3.7158]
    values = [1.381, 1.8866, 9.6903]

    y_ = []
    for xi in y:
        y_.append(1/xi)
    
    x_ = []
    for yi in x:
        x_.append(1/(yi**2))

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
        print(f'y(x{xi+1}) = {a*(values[xi]**2/(values[xi]**2 + b))}')


    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti) for ti in t]

    plt.plot(t, pt)
    plt.savefig('best_poly.png')