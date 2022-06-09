import numpy as np

#BEST_POLY

#FUNC EQUIVALENTE
# sqrt( y ) = 1/b + a/b * 1/sqrt( x )

'''
Um pesquisador relatou os dados tabulados a seguir.
Sabe-se que tais dados podem ser modelados pela seguinte equação: 
y=(a+x-√bx-√)2
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
    

    x = [0.5923, 1.4755, 2.7423, 2.8784, 4.3162, 5.0501, 5.8835, 6.3047, 6.9618, 7.9373, 8.7276, 9.8161]
    y = [20.4277, 9.6109, 5.8932, 5.7772, 4.2956, 3.6791, 3.4509, 3.3288, 3.0964, 2.9156, 2.7063, 2.6095]
    values = [1.9568, 7.5541, 8.2874]

    y_ = np.sqrt(y)
    
    x_ = 1/np.sqrt(x)

    grau = 1

    coefs = best_poly(x_, y_, grau)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    b = 1/a0
    a = a1 * b

    p = build_func(coefs)

    n = len(coefs)

    for xi in range(n):
        print(f'a{xi} = [{coefs[xi]}]')

    print(f'a = {a} b = {b}')

    n = len(values)
    for xi in range(n):
        print(f'y(x{xi+1}) = {(a0 + a1 * 1/np.sqrt(values[xi]))**2}')


    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti) for ti in t]

    plt.plot(t, pt)
    plt.savefig('best_poly.png')