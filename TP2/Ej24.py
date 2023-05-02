class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.__elements == stack_aux.__elements
        else:
            return False

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato

    def size(self):
        return len(self.__elements)

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]
        
'''Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:

A. Determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
ción uno la cima de la pila;
B. Determinar los personajes que participaron en más de 5 películas de la saga, además indi-
car la cantidad de películas en la que aparece;
C. Determinar en cuantas películas participo la Viuda Negra (Black Widow);
D. Mostrar todos los personajes cuyos nombre empiezan con C, D y G.'''

personajes = [
    {'Nombre': 'Capitán América', 'Peliculas': 8},
    {'Nombre': 'Hulk', 'Peliculas': 5},
    {'Nombre': 'Viuda Negra', 'Peliculas': 7},
    {'Nombre': 'Spider-Man', 'Peliculas': 5},
    {'Nombre': 'Rocket Raccoon', 'Peliculas': 5},
    {'Nombre': 'Doctor Strange', 'Peliculas': 3},
    {'Nombre': 'Captain Marvel', 'Peliculas': 2},
    {'Nombre': 'Loki', 'Peliculas': 6},
    {'Nombre': 'Thanos', 'Peliculas': 4},
    {'Nombre': 'Groot', 'Peliculas': 4},
    {'Nombre': 'Gamora', 'Peliculas': 3},
    {'Nombre': 'Nebula', 'Peliculas': 4},
]

pila_personajes = Pila()
for personaje in personajes:
    pila_personajes.push(personaje)

contador = len(personajes)
for personaje_actual in reversed(personajes):
    if personaje_actual['Nombre'] == 'Rocket Raccoon':
        posicion_rocket = contador
    if personaje_actual['Nombre'] == 'Groot':
        posicion_groot = contador
    contador -= 1
print(f"Rocket Raccoon se encuentra en la posición {posicion_rocket}")
print(f"Groot se encuentra en la posición {posicion_groot}")

print("Personajes que participaron en más de 5 películas:")
for personaje in personajes:
    if personaje['Peliculas'] > 5:
        print(f"{personaje['Nombre']} ({personaje['Peliculas']} películas)")

for personaje in personajes:
    if personaje['Nombre'] == 'Viuda Negra':
        print(f"La Viuda Negra participó en {personaje['Peliculas']} películas")
        
print("Personajes cuyos nombres empiezan con C, D y G:")
for personaje in personajes:
    if personaje['Nombre'][0] in ['C', 'D', 'G']:
        print(personaje['Nombre'])
