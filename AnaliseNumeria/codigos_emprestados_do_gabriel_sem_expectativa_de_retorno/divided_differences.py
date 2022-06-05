import math
x = [1.5402, 1.6131, 1.7921]

def f(x):
    return math.sqrt(math.cos(x**2) + x)

y = [f(i) for i in x]


def divided_differences(x,y):
    Y = [item for item in y]
    n = len(y)
    coeffs = [y[0]] + [0] * (n-1)
    for i in range(n-1):
        for j in range(n-1-i):
            numer = Y[j+1] - Y[j]
            denom = x[j+1+i] - x[j]
            Y[j] = numer / denom
        coeffs[i+1] = Y[0]
    return coeffs

coeffs = divided_differences(x,y)

def eq(x, coeffs):
    n = len(x)
    equation = ''
    for i in range(n):
        sign = ''
        if i != 0:
            sign = "*"
        equation += f'{coeffs[i]:+}{sign}'+'*'.join([f'(x{-xj:+})' for j, xj in enumerate(x) if j<i])
    return equation

print(coeffs)
eq = eq(x, coeffs)
#print('p(x) = ', eq)