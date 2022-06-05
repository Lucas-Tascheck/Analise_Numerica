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
    return a * 2**(b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


def modelo(x):
    a, b = -40, -30
    erro = a + (b - a) * np.random.random()
    return 2.5 * np.e ** (1.47 * x) + erro

if __name__ == '__main__':

    
   
    x = [0.049, 0.0811, 0.1154, 0.2015, 0.2521, 0.2808, 0.3464, 0.4049, 0.4799, 0.5535, 0.6065, 0.645, 0.7193, 0.7408, 0.817, 0.8734, 0.9172, 0.9986, 1.0542, 1.0954, 1.1422, 1.2217, 1.251, 1.3047, 1.3605, 1.4101, 1.4554, 1.5288, 1.5781, 1.6207, 1.691, 1.7325, 1.7962, 1.8736, 1.9035, 1.9462]
    y = [5.2176, 5.292, 3.5493, 6.1172, 6.7886, 6.7616, 8.3817, 8.5148, 10.1594, 10.2612, 10.621, 11.261, 13.2145, 10.8265, 14.2494, 15.4753, 18.8916, 18.696, 22.5838, 21.3234, 23.199, 22.7247, 26.2961, 26.843, 30.9238, 35.9493, 35.5703, 39.3973, 41.4473, 44.4411, 46.7947, 54.3445, 56.5489, 64.4552, 66.156, 68.9782]
    values = [0.0696, 0.5674, 0.7089, 1.123, 1.9012]


    #transladar os pontos para cima
    k = abs(min(y)) + 1
    yt = [yi + k for yi in y]

    y_ = np.log(y)

    grau = 1

    a0, a1 = best_poly(x, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1/np.log(2)

    print(f'{a = } e {b = }')

    n = len(values)
    somas = []
    for xi in range(n):
        print(a * 2**(b*values[xi]))

    p = build_func(a, b)

    def q(x):
        return p(x) - k


    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt, color='r')
    plt.savefig('best_exp.png')