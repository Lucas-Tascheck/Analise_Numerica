import math

def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma

def f(x):
    return math.e ** (- x ** 2)


x = [0.119, 0.189, 0.292, 0.471, 0.526, 0.54, 0.687, 1.088, 1.103, 1.105, 1.688, 1.909, 2.588, 2.745, 3.048, 3.179, 3.22, 3.466, 4.188, 4.781, 4.893]
y = [1.614, 1.862, 2.222, 2.72, 2.824, 2.847, 2.988, 2.739, 2.721, 2.718, 2.097, 2.008, 2.339, 2.527, 2.89, 2.984, 2.997, 2.837, 1.003, 2.993, 2.87]

total = 0
def trap(x1,x2,y1,y2):
    return (( y1 + y2 )/2 ) * (x2-x1)
#for i in range(1,len(x)):
    #total += trap(x[i-1],x[i],y[i-1],y[i])
#print(total)
