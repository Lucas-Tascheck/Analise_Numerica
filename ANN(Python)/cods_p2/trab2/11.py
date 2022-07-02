import numpy as np

#BEST_EXP

'''
Encontre os coeficientes a e b da função exponencial y=aebx que melhor se aproxima da seguinte lista de 12 pontos
(0.1108,5.6869)
, (0.3323,9.5643), (0.3849,9.2412), (0.5644,12.8301), (0.6762,18.6405), (0.9608,33.0995), (1.0203,35.8162), (1.3164,64.0706), (1.4996,92.8868), (1.5227,95.3317), (1.6749,128.9468) e (1.9595,221.9305)
Em seguida, calcule o valor de y para os seguintes valores de x:
x1=1.0355
, x2=1.2819 e x3=1.6745
'''

#func: log(y) = log(a) + bx * log

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
    return a * np.exp(b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


def modelo(x):
    a, b = -40, -30
    erro = a + (b - a) * np.random.random()
    return 2.5 * np.e ** (1.47 * x) + erro

if __name__ == '__main__':

 
    x = [0.1411, 0.3067, 0.3707, 0.5932, 0.832, 0.9099, 1.0538, 1.1879, 1.4631, 1.6583, 1.7317, 1.8401]
    y = [4.9657, 7.4502, 8.2596, 13.3869, 20.5913, 23.3411, 31.1683, 40.5779, 68.9733, 103.5134, 116.2897, 143.1011]
    values = [0.9999, 1.4494, 1.7635]


    #transladar os pontos para cima
    k = abs(min(y)) + 1
    yt = [yi + k for yi in y]

    y_ = np.log(y)

    grau = 1

    a0, a1 = best_poly(x, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1

    print(f'{a = } e {b = }')

    n = len(values)
    somas = []
    for xi in range(n):
        print(a * np.exp(b * values[xi]))

    p = build_func(a, b)

    def q(x):
        return p(x) - k


    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt, color='r')
    plt.savefig('best_exp.png')