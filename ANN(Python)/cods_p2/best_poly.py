import numpy as np

#BEST_POLY

#FUNC EQUIVALENTE
# sqrt( y ) = 1/b + a/b * 1/sqrt( x )

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
    

    x = [-4.8174, -4.5498, -4.2816, -3.8042, -3.6765, -3.2345, -2.9636, -2.7085, -2.338, -2.054, -1.7454, -1.1532, -0.9302, -0.7423, -0.4141, 0.1764, 0.2011, 0.703, 1.0717, 1.3305, 1.6295, 2.0662, 2.3542, 2.5953, 3.0371, 3.2051, 3.7138, 3.8079, 4.2658, 4.4701, 4.7093, 5.0924, 5.4628, 5.7807]
    y = [3.1932, 3.6985, 3.1095, 4.5305, 4.6413, 5.0488, 5.5694, 4.5107, 5.6161, 5.6464, 5.5075, 5.1567, 4.9435, 4.9024, 4.5009, 4.2421, 3.9218, 3.9524, 3.4879, 3.2988, 3.2695, 2.9728, 2.9708, 3.0959, 3.0129, 4.1019, 3.6758, 4.0691, 4.6697, 4.641, 5.4949, 5.7501, 7.2344, 8.1487]

    grau = 3

    coefs = best_poly(x, y, grau)

    p = build_func(coefs)

    n = len(coefs)

    for xi in range(n):
        print(f'a{xi} = [{coefs[xi]}]')


    #n = len(values)
    #for xi in range(n):
        #print(f'y(x{xi+1}) = {a/(np.sqrt(1+2*b*(a**2)*values[xi]))}')


    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti) for ti in t]

    plt.plot(t, pt)
    plt.savefig('best_poly.png')