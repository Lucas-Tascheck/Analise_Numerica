import numpy as np

#BEST_POT

'''
Encontre os coeficientes a e b da função potência y=axb que melhor se aproxima da seguinte lista de 12 pontos
(0.6168,1.2651)...
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


def poly(x, a, b):
    return a * x ** b

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


def modelo(x):
    a, b = 1, 5
    erro = a + (b - a) * np.random.random()
    return 1.36 * x ** 3.89 + erro

if __name__ == '__main__':


    x = [0.6168, 0.8116, 1.0133, 1.2433, 1.4222, 1.5527, 1.8941, 2.0144, 2.3082, 2.4888, 2.6954, 2.8403]
    y = [1.2651, 0.9344, 2.5704, 4.8085, 6.9219, 9.7271, 18.2057, 21.9863, 33.3691, 42.9891, 54.2406, 64.1018]
    values = [0.8076, 2.2984, 2.807]


    x_ = np.log(x)
    y_ = np.log(y)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1

    print(f'{a = } e {b = }')

    p = build_func(a, b)

    n = len(values)
    somas = []
    for xi in range(n):
        print(f'y(x{xi+1}) = {a * values[xi]**b}')



    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti) for ti in t]

    plt.plot(t, pt, color='r')
    plt.savefig('best_pot.png') 