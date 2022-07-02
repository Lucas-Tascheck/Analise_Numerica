import numpy as np

#BEST_EXP

'''
Encontre os coeficientes a e b da função exponencial y=a2bx que melhor se aproxima da seguinte lista de 36 pontos
(0.049,5.2176)...
'''

#func: log(y) = log(a) + b * log(2) * x

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

    
 
    x = [0.0261, 0.0566, 0.155, 0.1774, 0.2311, 0.3006, 0.3442, 0.4233, 0.4662, 0.5021, 0.5833, 0.6608, 0.6696, 0.7541, 0.8049, 0.8346, 0.9179, 0.9671, 1.0359, 1.0944, 1.1202, 1.1705, 1.2636, 1.3066, 1.346, 1.4016, 1.4743, 1.5526, 1.5765, 1.6231, 1.7158, 1.7649, 1.8161, 1.8548, 1.9255, 1.9896]
    y = [5.7646, 4.7688, 5.5268, 5.9421, 5.3846, 5.0252, 7.9104, 7.7102, 8.2169, 9.2028, 9.0336, 10.1209, 9.7324, 10.6844, 11.2987, 11.2282, 12.649, 13.5321, 14.0327, 13.653, 13.1693, 18.6008, 17.2411, 19.3919, 17.1589, 22.4036, 23.2399, 22.1063, 24.6962, 26.3858, 29.1824, 32.1166, 33.152, 32.6928, 36.7824, 37.5386]
    values = [0.2038, 1.2172, 1.2918, 1.389, 1.8877]


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