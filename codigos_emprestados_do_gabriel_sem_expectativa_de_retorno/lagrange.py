import math

def lagrange(x, y):
    n = len(x)
    if n == len(y):
        eq = ''
        for k in range(n):
            numer = '*'.join( [f'(x{-xi:+})' for i, xi in enumerate(x) if i != k] )
            denom = '*'.join( [f'({x[k]}{-xi:+})' for i, xi in enumerate(x) if i != k] )
            eq += f'{y[k]:+}*({numer})/({denom}) '
            a = y[k]
            print(eval('a/('+denom+')'))
            
        return eq
    else:
        raise TypeError('O num de coords x é dif de num de coords y')


def f(x):
    return x ** 5 - 4*x**2 + 2*(math.sqrt(x+1)) + math.cos(x)

x = [-0.396, -0.179, -0.025, 0.08, 0.331, 0.486, 0.71, 0.816, 1.005, 1.159, 1.407]
y = [f(i) for i in x]


eq = lagrange(x,y)
#print(eq)
def subs(x):
    return eval(eq)
for i in range(len(values)):
    print(f(values[i]) - subs(values[i]) )
