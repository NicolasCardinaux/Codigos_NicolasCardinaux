'''Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

a. de cada una de las maravillas se conoce su name, país de ubicación (puede ser más de
uno en las naturales) y types (natural o arquitectónica);
b. cada una debe estar relacionada con las otras seis de su types, para lo que se debe almacenar
la distancia que las separa;
c. hallar el árbol de expansión mínimo de cada types de las maravillas;
d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
e. determinar si algún país tiene más de una maravilla del mismo types;
f. deberá utilizar un grafo no dirigido.'''
from grafo import Grafo01
from random import randint

# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:


class Maravilla:
    def __init__(self, name, country, types):
        self.name = name
        self.country = country if isinstance(country, list) else [country]
        self.types = types

    def __str__(self):
        return f"Nombre: {self.name}, Países: {', '.join(self.country)}, Tipo: {self.types}"

# A. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
maravillas_naturales = [
    Maravilla("Aurora Boreal", "Varios lugares del Ártico", "natural"),
    Maravilla("Gran Cañón", "Estados Unidos", "natural"),
    Maravilla("Gran Barrera de Coral", "Australia", "natural"),
    Maravilla("Parque Nacional de Yellowstone", "Estados Unidos", "natural"),
    Maravilla("Cataratas del Iguazú", "Argentina", "natural"),
    Maravilla("Monte Everest", "Nepal", "natural"),
]

# Ahora, puedes utilizar estas maravillas naturales con las mismas distancias aleatorias en el grafo


maravillas_arquitectonicas = [
    Maravilla("Gran Pirámide de Guiza", "Egipto", "arquitectónica"),
    Maravilla("Taj Mahal", "India", "arquitectónica"),
    Maravilla("Gran Muralla China", "China", "arquitectónica"),
    Maravilla("Coliseo Romano", "Italia", "arquitectónica"),
    Maravilla("Estatua de la Libertad", "Estados Unidos", "arquitectónica"),
    Maravilla("Teatro Colón", "Argentina", "arquitectónica"),
]

dic = {}

for i in range(6):
    dic[maravillas_arquitectonicas[i].name] = i
    dic[maravillas_naturales[i].name] = i

# F. deberá utilizar un grafo no dirigido.
mi_grafo = Grafo01(dirigido=False)

for i in maravillas_arquitectonicas:
    mi_grafo.insert_vertice(i.name)

for i in maravillas_naturales:
    mi_grafo.insert_vertice(i.name)

# conecto las aristas y chequeo que no se repitan     
# B. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
for i in maravillas_arquitectonicas:
    valor_i = mi_grafo.search_vertice(i.name)
    posicion_uno = mi_grafo.get_element_by_index(valor_i)
    for j in maravillas_arquitectonicas:
        valor_j = mi_grafo.search_vertice(j.name)
        posicion_dos = mi_grafo.get_element_by_index(valor_j)
        if posicion_uno != posicion_dos:
            if not mi_grafo.is_adyacent(posicion_uno[0], posicion_dos[0]):
                value = randint(100, 5000)
                mi_grafo.insert_arist(posicion_uno[0], posicion_dos[0], value)
         

for i in maravillas_naturales:
    valor_i = mi_grafo.search_vertice(i.name)
    posicion_uno = mi_grafo.get_element_by_index(valor_i)
    for j in maravillas_naturales:
        valor_j = mi_grafo.search_vertice(j.name)
        posicion_dos = mi_grafo.get_element_by_index(valor_j)
        if posicion_uno != posicion_dos:
            if not mi_grafo.is_adyacent(posicion_uno[0], posicion_dos[0]):
                value = randint(100, 5000)
                mi_grafo.insert_arist(posicion_uno[0], posicion_dos[0], value)
        
print('--------------------------------------------------------------------------------')

# C. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
print('Punto C')
bosque = mi_grafo.kruskal()
for i, arbol in enumerate(bosque, start=1):
    print(f"Árbol de expansión mínima {i} para el tipo de maravilla:")
    for nodo in arbol.split(";"):
        print(nodo)
    print()

print('--------------------------------------------------------------------------------')       
#D. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
print('Punto D')

countries_with_both_types = set()

for maravilla in maravillas_naturales:
    for país in maravilla.country:
        for otra_maravilla in maravillas_arquitectonicas:
            if país in otra_maravilla.country:
                countries_with_both_types.add(país)

if countries_with_both_types:
    print("Países que disponen de maravillas arquitectónicas y naturales:")
    for país in countries_with_both_types:
        print(país)

print('--------------------------------------------------------------------------------')

# E. determinar si algún país tiene más de una maravilla del mismo tipo;
print('Punto E')
nature_countries = set()
non_nature_countries = set()

for maravilla in maravillas_arquitectonicas + maravillas_naturales:
    for país in maravilla.country:
        if maravilla.types == "natural":
            if país in nature_countries:
                print(f"{país} tiene más de una maravilla natural")
            else:
                nature_countries.add(país)
        elif maravilla.types == "arquitectónica":
            if país in non_nature_countries:
                print(f"{país} tiene más de una maravilla arquitectónica")
            else:
                non_nature_countries.add(país)
print('--------------------------------------------------------------------------------') 
