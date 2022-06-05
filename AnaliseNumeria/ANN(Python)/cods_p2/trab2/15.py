from re import A
import numpy as np

#BEST_EXP

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


def poly(x, a, b):
    return a*x*np.exp(b*x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


def modelo(x):
    a, b = -40, -30
    erro = a + (b - a) * np.random.random()
    return 2.5 * np.e ** (1.47 * x) + erro

if __name__ == '__main__':

  
    x = [0.8185, 1.2928, 2.2279, 3.1632, 3.5466, 4.5674, 5.2296, 6.5431, 7.0307, 8.3205, 9.0334, 9.8746]
    y = [2.6099, 3.6357, 4.9531, 5.5947, 5.7257, 5.6535, 5.4748, 5.0963, 4.6968, 4.0971, 3.6815, 3.2395]
    values = [5.4764, 8.7468, 9.2214]


    #transladar os pontos para cima
    k = abs(min(y)) + 1
    yt = [yi + k for yi in y]

    y_ = np.log(y) - np.log(x)

    grau = 1

    a0, a1 = best_poly(x, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1

    print(f'{a = } e {b = }')

    n = len(values)
    somas = []
    for xi in range(n):
        print(f'y(x{xi+1}) = {a*values[xi]*np.exp(b*values[xi])}')

    p = build_func(a, b)

    def q(x):
        return p(x) - k


    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt, color='r')
    plt.savefig('best_exp.png')