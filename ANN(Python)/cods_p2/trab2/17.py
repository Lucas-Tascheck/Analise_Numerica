from re import A
import numpy as np

#BEST_EXP

'''
Um pesquisador relatou os dados tabulados a seguir.
Sabe-se que tais dados podem ser modelados pela seguinte equação: 
x=e(y-b)/a
onde a e b são parâmetros. 
Use uma transformação para linearizar essa equação e use regressão linear para encontrar os valores de a e b. 
Em seguida, calcule o valor de y para os seguintes valores de x:
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


    x = [1.0445, 2.0942, 3.2285, 3.5387, 4.5158, 5.0343, 5.7365, 6.8186, 7.4631, 8.1934, 9.0997, 9.5306]
    y = [2.739, 3.6265, 4.1648, 4.2997, 4.6447, 4.7612, 4.8353, 4.9536, 5.2446, 5.4341, 5.3349, 5.5644]
    values = [3.6269, 7.7709, 7.9576]

    #transladar os pontos para cima
    k = abs(min(y)) + 1
    yt = [yi + k for yi in y]

    x_ = np.log(x)

    y_ = y

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = a1
    b = a0

    print(f'{a = } e {b = }')

    n = len(values)
    somas = []
    for xi in range(n):
        print(f'y(x{xi+1}) = {a0+a1*np.log(values[xi])}')

    p = build_func(a, b)

    def q(x):
        return p(x) - k


    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt, color='r')
    plt.savefig('best_exp.png')