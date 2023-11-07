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

# Crear un grafo no dirigido
graph = Grafo01(dirigido=False)

# Definir los nombres de los ambientes de la casa
habitaciones = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

# Insertar vértices en el grafo para representar los ambientes de la casa
for i in habitaciones:
    graph.insert_vertice(i)

j = 0

# Cargar al menos tres aristas a cada vértice, con pesos aleatorios
for i in habitaciones:
    position = graph.search_vertice(i)
    point = graph.get_element_by_index(position)

    if point[1].size() < 3:
        k = 0
        while j == 0:
            if k >= len(habitaciones):
                j = 1
            else:
                place = habitaciones[k]
                positionb = graph.search_vertice(place)
                pointb = graph.get_element_by_index(positionb)
                checker = graph.is_adyacent(point[0], pointb[0])
                graph.mark_as_not_visited()

                if pointb[1].size() < 3 and point[0] != pointb[0] and not checker:
                    value = randint(1, 11)
                    graph.insert_arist(point[0], pointb[0], value)

                    if point[1].size() == 3:
                        j = 1

                k += 1
        j = 0

# Cargar algunas aristas adicionales entre ambientes específicos
val = uniform(1, 11)
value = randint(1, 11)
graph.insert_arist("patio", "cochera", value)
val = uniform(1, 11)
value = randint(1, 11)
graph.insert_arist("cochera", "sala de estar", value)
val = uniform(1, 11)
value = randint(1, 11)
graph.insert_arist("baño 1", "comedor", value)
val = uniform(1, 11)
value = randint(1, 11)
graph.insert_arist("comedor", "terraza", value)

# Calcular el árbol de expansión mínima y la cantidad de metros de cables necesarios
graph.mark_as_not_visited()
min_exp = graph.kruskal()
total_cable = 0
for i in min_exp:
    k = i.split(";")
    for j in k:
        total_cable += int(j.split("-")[2])
print(f"Se necesitan {total_cable} metros de cable para conectar todos los ambientes")

# Calcular el camino más corto desde la habitación 1 hasta la sala de estar y la cantidad de metros de cable de red necesarios
graph.mark_as_not_visited()
path = graph.dijkstra("habitación 1", "sala de estar")
i = 0
while i != 1:
    value = path.pop()
    if value[0] == "sala de estar":
        i = 1

print(f"Se necesitan {value[1]} metros para conectar el router con el Smart TV desde la habitación 1 hasta la sala de estar")
