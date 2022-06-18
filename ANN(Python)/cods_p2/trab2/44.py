import math


def quadratura(f, x, c):
    return sum([ci * f(xi) for ci, xi in zip(c, x)])

def change(f, a, b):
    def g(u):
        return f(a + (b - a) * (u + 1) / 2) * (b - a) / 2
    return g


if __name__ == '__main__':


    #exemplo 1
    nos = (
[0, -0.5384693101056831, 0.5384693101056831, -0.906179845938664, 0.906179845938664]
    )
    pesos = (
[0.5688888888888889, 0.47862867049936647, 0.47862867049936647, 0.23692688505618908, 0.23692688505618908]
    )

    def f_1(x):
        return (x+1/x)**2
      
    a, b = 0.552, 2.931
    g = change(f_1, a, b)

    aprox_1 = quadratura(g, nos, pesos)
    print(f'A = {aprox_1 = }')