'''Implementar sobre un graph no dirigido los algoritmos necesario para dar solución a las si-
guientes tareas:

a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
ta es la distancia entre los ambientes, se debe cargar en metros;

c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv.'''
from grafo import Grafo01
from random import uniform, randint
# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

mi_grafo = Grafo01(dirigido=False)

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
mi_grafo.insert_vertice('cocina')
mi_grafo.insert_vertice('comedor')
mi_grafo.insert_vertice('cochera')
mi_grafo.insert_vertice('quincho')
mi_grafo.insert_vertice('baño 1')
mi_grafo.insert_vertice('baño 2')
mi_grafo.insert_vertice('habitación 1')
mi_grafo.insert_vertice('habitación 2')
mi_grafo.insert_vertice('sala de estar')
mi_grafo.insert_vertice('terraza')
mi_grafo.insert_vertice('patio')

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

mi_grafo.insert_arist('cocina', 'cochera', 10)
mi_grafo.insert_arist('cocina', 'comedor', 10)
mi_grafo.insert_arist('cocina', 'quincho', 5)
mi_grafo.insert_arist('baño 1', 'comedor', 7)
mi_grafo.insert_arist('baño 1', 'cochera', 3)
mi_grafo.insert_arist('baño 1', 'quincho', 3)
mi_grafo.insert_arist('baño 2', 'comedor', 11)
mi_grafo.insert_arist('baño 2', 'cochera', 7)
mi_grafo.insert_arist('baño 2', 'quincho', 6)
mi_grafo.insert_arist('habitación 1', 'terraza', 10)
mi_grafo.insert_arist('habitación 1', 'patio', 10)
mi_grafo.insert_arist('habitación 1', 'comedor', 11)
mi_grafo.insert_arist('habitación 2', 'terraza', 9)
mi_grafo.insert_arist('habitación 2', 'patio', 4)
mi_grafo.insert_arist('habitación 2', 'comedor', 4)
mi_grafo.insert_arist('sala de estar', 'terraza', 11)
mi_grafo.insert_arist('sala de estar', 'patio', 6)
mi_grafo.insert_arist('sala de estar', 'comedor', 5)
mi_grafo.insert_arist('sala de estar', 'baño 1', 6)
mi_grafo.insert_arist('sala de estar', 'baño 2', 5)

print('--------------------------------------------------------------------------------')

# c. obtener el árbol de expansión mínima
print('Punto C:')
min_exp = mi_grafo.kruskal()
print(min_exp)
total_cable = 0
for i in min_exp:
    k=i.split(";")
    for j in k:
        total_cable = total_cable + int(j.split("-")[2])
print()
print(f"Se necesitan {total_cable} metros de cable, para conectar todos los ambientes")

print('--------------------------------------------------------------------------------')

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

path = mi_grafo.dijkstra("habitación 1","sala de estar")
i=0
while i != 1:
    value = path.pop()
    if value[0] == "sala de estar":
        i = 1
print('Punto D:')
print(f"Se necesitan {value[1]} metros para conectar el router con el Smart TV")

print('--------------------------------------------------------------------------------')
