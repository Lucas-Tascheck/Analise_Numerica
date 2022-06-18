import math


def quadratura(f, x, c):
    return sum([ci * f(xi) for ci, xi in zip(c, x)])

def change(f, a, b):
    def g(u):
        return f(a + (b - a) * (u + 1) / 2) * (b - a) / 2
    return g


if __name__ == '__main__':


    #exemplo 1
    x = ([-0.33998104358485626, 0.33998104358485626, -0.8611363115940526, 0.8611363115940526])
    c = ([0.6521451548625461, 0.6521451548625461, 0.34785484513745385, 0.34785484513745385])

    def f_1(x):
        return (9 + 4*(math.cos(0.49*x)**2))*(5*math.exp(-0.52*x) + 2*math.exp(0.18*x))

    a = 2.74
    b = 7.69

    g = change(f_1, a, b)

    aprox_1 = quadratura(g, x, c)

    print(f'{aprox_1}')

