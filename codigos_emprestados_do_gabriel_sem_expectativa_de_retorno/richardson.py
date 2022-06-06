import math

def richardson(col1):
    col1 = [item for item in col1]
    n = len(col1)
    for j in range(n -1):
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j):
            power = j + 1
            temp_col[i] = (2 ** power * col1[i+1] - col1[i]) / (2 ** power - 1)
        col1[:n -1 - j] = temp_col
    return col1[0]

def F1(f, x0, h):
    return (f(x0 + h) - f(x0)) / h

def f(x):
    return math.sin( math.sqrt(math.pi + x ** 2) )

x0 = 0.44438
h = 9
col1 = [-0.24119906143771708, -0.2893017661778359, -0.30286988618973965, -0.30637062313599017]
r = richardson(col1)
print(r)

def F2(f, x0, h):
    return (f(x0) - f(x0 - h)) / h

def g(x):
    return math.cos(2 ** x)

x0 = 1
h = 0.437
col1 = [F2(g, x0, h / 2 ** i) for i in range(10)]
print(col1)

