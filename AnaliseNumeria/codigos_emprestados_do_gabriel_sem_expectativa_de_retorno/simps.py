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
    return math.exp(-x ** 2)


x = [0.53, 0.67, 0.81, 0.8505, 0.891, 1.0955, 1.3, 1.369, 1.438, 1.6795, 1.921, 2.562, 3.203, 3.3655, 3.528, 3.6145, 3.701, 3.76, 3.819, 3.8985, 3.978, 4.467, 4.956]
y = [2.831, 2.98, 2.988, 2.969, 2.942, 2.73, 2.471, 2.388, 2.311, 2.103, 2.006, 2.311, 2.992, 2.957, 2.722, 2.51, 2.246, 2.044, 1.834, 1.554, 1.303, 1.804, 2.634]

total = 0
def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)
for i in range(0,11*2,2):
    total += simp(x[i],x[i+1],x[i+2],y[i],y[i+1],y[i+2])
print(total)