import numpy as np

#exemplos
x = [0, np.pi / 2, np.pi]
y = [0, 1, 0]

def poly(x, y):
    n = len(x) - 1
    a = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi ** j)
        a.append(row)
    return np.linalg.solve(a, y)


def func_poly(x, coeffs):
    first = coeffs[0]
    return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:], 1)])



if __name__== '__main__':
    coeffs = poly(x, y)
    print(coeffs)

    def p(x):
        return func_poly(x, coeffs)

    #visualizacao
    import matplotlib.pylab as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti) for ti in t]
    st = np.sin(t)

    plt.plot(t, pt)
    plt.plot(t, st)

    plt.savefig('interp.png')

