import math

def double_trapz(f, a: float, b: float, c:float, d: float, n1: float, n2: float) -> float:
    if n1 <= 0 or n2 <= 0:
      raise ValueError('Ops, isso não pode')
    h1 = (b - a) / n1
    h2 = (d - c) / n2
    soma_interior = 0
    for i in range(1, n1):
      for j in range(1, n2):
        soma_interior += f(a + i * h1, c + j * h2)
    soma_arestas_horizontais = 0
    for i in range(1, n1):
      for j in [0, n2]:
        soma_arestas_horizontais += f(a + i * h1, c + j * h2)
    soma_arestas_verticais = 0  
    for j in range(1, n2):
      for i in [0, n1]:
        soma_arestas_verticais += f(a + i * h1, c + j * h2)
    soma_vertices = 0
    for i in [0, n1]:
      for j in [0, n2]:
        soma_vertices += f(a + i * h1, c + j * h2)
    return (h1 * h2 / 4) * (soma_vertices + 4 * soma_interior + 2 * (soma_arestas_horizontais + soma_arestas_verticais))
    
def f(x, y):
    return math.exp(-(x + y)**2)

intervalo1 = [-0.714, 1.035]
intervalo2 = [-0.642, 0.518]
n1 = 8
n2 = 7


r = double_trapz(f, intervalo1[0], intervalo1[1], intervalo2[0], intervalo2[1], n1, n2)

print(r)
