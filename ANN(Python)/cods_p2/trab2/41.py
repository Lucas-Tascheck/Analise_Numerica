import math

def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))

def f(x):
    return math.sqrt(1 + math.cos(x)**2)

def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'{somas}')



x = [0.239, 0.6325, 1.026, 1.512, 1.998, 2.247, 2.496, 2.842, 3.188, 3.259, 3.33, 3.4265, 3.523, 3.816, 4.109, 4.205, 4.301, 4.4425, 4.584, 4.6135, 4.643]
y = [2.04, 2.956, 2.813, 2.236, 2.0, 2.061, 2.244, 2.651, 2.987, 3.0, 2.98, 2.894, 2.733, 1.844, 1.035, 1.011, 1.165, 1.688, 2.384, 2.52, 2.646]


intervalo = [-1.091, 1.438]
subintervalos = [4, 18, 32, 60, 98, 108, 132, 152, 194, 212, 278]

'''
n = len(subintervalos)
for i in range(n):
    print(simps(f, intervalo[0], intervalo[1], subintervalos[i]))
'''

simpsPonto(x, y)



