# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

# a. de cada una de las maravillas se conoce su name, país de ubicación (puede ser más de
# uno en las naturales) y types (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su types, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada types de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo types;
# f. deberá utilizar un grafo no dirigido.
# Importa la clase Grafo01 del módulo grafo y la función randint del módulo random
from grafo import Grafo01
from random import randint

class Maravilla:
    def __init__(self, name, country, types):
        self.name = name
        self.country = country if isinstance(country, list) else [country]
        self.types = types

    def add_pais(self, pais):
        self.country.append(pais)

    def __str__(self):
        return f"Nombre: {self.name}, Países: {', '.join(self.country)}, Tipo: {self.types}"

maravillas_naturales = [
    Maravilla("Cataratas del Iguazú", ["Argentina", "Brasil"], "natural"),
    Maravilla("Gran Cañón", "Estados Unidos", "natural"),
    Maravilla("Gran Barrera de Coral", "Australia", "natural"),
    Maravilla("Aurora Boreal", ["Varios lugares del Ártico"], "natural"),
    Maravilla("Monte Everest", ["Nepal", "Tíbet"], "natural"),
    Maravilla("Parque Nacional de Yellowstone", "Estados Unidos", "natural")
]

maravillas_arquitectonicas = [
    Maravilla("Gran Pirámide de Guiza", "Egipto", "arquitectónica"),
    Maravilla("Gran Muralla China", "China", "arquitectónica"),
    Maravilla("Taj Mahal", "India", "arquitectónica"),
    Maravilla("Estatua de la Libertad", "Estados Unidos", "arquitectónica"),
    Maravilla("Coliseo Romano", "Italia", "arquitectónica"),
    Maravilla("Ciudad de Petra", "Jordania", "arquitectónica")
]

dic = {}

for i in range(6):
    dic[maravillas_arquitectonicas[i].name] = i
    dic[maravillas_naturales[i].name] = i

new_graph = Grafo01(dirigido=False)

for i in maravillas_arquitectonicas:
    new_graph.insert_vertice(i.name)

for i in maravillas_naturales:
    new_graph.insert_vertice(i.name)

# Punto a: Conecta las maravillas arquitectónicas entre sí con distancias aleatorias
for i in maravillas_arquitectonicas:
    positiona = new_graph.search_vertice(i.name)
    pointa = new_graph.get_element_by_index(positiona)
    for j in maravillas_arquitectonicas:
        positionb = new_graph.search_vertice(j.name)
        pointb = new_graph.get_element_by_index(positionb)
        checker = new_graph.is_adyacent(pointa[0], pointb[0])
        if pointa != pointb and checker == False:
            value = randint(100, 5000)
            new_graph.insert_arist(pointa[0], pointb[0], value)

# Punto b: Conecta las maravillas naturales entre sí con distancias aleatorias
for i in maravillas_naturales:
    positiona = new_graph.search_vertice(i.name)
    pointa = new_graph.get_element_by_index(positiona)
    for j in maravillas_naturales:
        positionb = new_graph.search_vertice(j.name)
        pointb = new_graph.get_element_by_index(positionb)
        checker = new_graph.is_adyacent(pointa[0], pointb[0])
        if pointa != pointb and checker == False:
            value = randint(100, 5000)
            new_graph.insert_arist(pointa[0], pointb[0], value)

# Punto c: Encuentra países que tienen ambos tipos de maravillas y los imprime
countries = []
for i in maravillas_naturales:
    positiona = new_graph.search_vertice(i.name)
    pointa = new_graph.get_element_by_index(positiona)
    for j in maravillas_arquitectonicas:
        positionb = new_graph.search_vertice(j.name)
        pointb = new_graph.get_element_by_index(positionb)
        index_A = dic[pointa[0]]
        index_B = dic[pointb[0]]
        if maravillas_arquitectonicas[index_B].country[0] in maravillas_naturales[index_A].country:
            if (maravillas_arquitectonicas[index_B].country in countries) == False:
                countries.append(maravillas_arquitectonicas[index_B].country)

# Imprime los países que tienen ambos tipos de maravillas
for i in countries:
    print(f"Punto c: {i[0]} posee los 2 tipos de maravilla")

# Punto d: Encuentra países con más de una maravilla del mismo tipo (naturales)
nature_2 = []
for i in maravillas_naturales:
    positiona = new_graph.search_vertice(i.name)
    pointa = new_graph.get_element_by_index(positiona)
    for j in maravillas_naturales:
        positionb = new_graph.search_vertice(j.name)
        pointb = new_graph.get_element_by_index(positionb)
        index_A = dic[pointa[0]]
        index_B = dic[pointb[0]]
        for k in maravillas_naturales[index_B].country:
            for l in maravillas_naturales[index_A].country:
                if k == l and pointb[0] != pointa[0]:
                    if (k in nature_2) == False:
                        nature_2.append(k)

# Imprime los países con 2 maravillas naturales del mismo tipo
for i in nature_2:
    print(f"Punto d: {i} posee 2 maravillas(naturaleza) del mismo tipo")

# Punto e: Encuentra países con más de una maravilla del mismo tipo (arquitectónicas)
non_nature_2 = []
for i in maravillas_arquitectonicas:
    positiona = new_graph.search_vertice(i.name)
    pointa = new_graph.get_element_by_index(positiona)
    for j in maravillas_arquitectonicas:
        positionb = new_graph.search_vertice(j.name)
        pointb = new_graph.get_element_by_index(positionb)
        index_A = dic[pointa[0]]
        index_B = dic[pointb[0]]
        for k in maravillas_arquitectonicas[index_B].country:
            for l in maravillas_arquitectonicas[index_A].country:
                if k == l and pointb[0] != pointa[0]:
                    if (k in non_nature_2) == False:
                        non_nature_2.append(k)

# Imprime los países con 2 maravillas arquitectónicas del mismo tipo
for i in non_nature_2:
    print(f"Punto e: {i} posee 2 maravillas(arquitectura) del mismo tipo")

# Punto f: Encuentra y muestra el árbol de expansión mínimo (MST) para cada tipo de maravilla
bosque = new_graph.kruskal()
for arbol in bosque:
    print('Punto f: Árbol de expansión mínimo (MST)')
    for nodo in arbol.split(';'):
        print(nodo)
