import numpy as np

#BEST_POT

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


    x = [0.0292, 0.6145, 0.7243, 1.1978, 1.5371, 1.7587, 1.9848, 2.4464, 2.6368, 2.9341, 3.4708, 3.7899, 3.9661, 4.5079, 4.5297, 4.8669, 5.2549, 5.5394, 5.9787, 6.1851, 6.6548, 6.7807, 7.2896, 7.5807, 7.9916, 8.3641, 8.5982, 8.7421, 9.2056, 9.4539, 9.7178]
    y = [6.1901, 5.3755, 5.3479, 5.1856, 2.9628, 4.7501, 4.7203, 4.3681, 4.5657, 4.1712, 3.9345, 4.1864, 4.0296, 3.9729, 4.876, 3.9424, 3.9052, 4.1176, 3.9363, 4.0502, 4.1546, 3.9833, 3.7586, 3.9847, 3.532, 5.5148, 4.6633, 5.2307, 5.0489, 5.2365, 4.7499]

    values = [0.8076, 2.2984, 2.807]


    x_ = x
    y_ = y

    grau = 2

    a0, a1 = best_poly(x, y, grau)

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