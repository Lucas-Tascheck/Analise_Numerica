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

    
    x = [0.1108, 0.3323, 0.3849, 0.5644, 0.6762, 0.9608, 1.0203, 1.3164, 1.4996, 1.5227, 1.6749, 1.9595]
    y = [5.6869, 9.5643, 9.2412, 12.8301, 18.6405, 33.0995, 35.8162, 64.0706, 92.8868, 95.3317, 128.9468, 221.9305]
    values = [1.0355, 1.2819, 1.6745]


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