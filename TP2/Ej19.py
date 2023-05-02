
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
        
        
'''Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de es-
treno, desarrollar las funciones necesarias para resolver las siguientes actividades:

a. mostrar los nombre películas estrenadas en el año 2014;
b. indicar cuántas películas se estrenaron en el año 2018;
c. mostrar las películas de Marvel Studios estrenadas en el año 2016.'''


pila_peliculas = Pila()

peliculas = [
    {'titulo': 'X-Men: Días del futuro pasado', 'estudio': 'Marvel Studios', 'año': 2014},
    {'titulo': 'Transformers: la era de la extinción', 'estudio': 'Paramount', 'año': 2014},
    {'titulo': 'Interstellar', 'estudio': 'Paramount', 'año': 2014},
    {'titulo': 'Los Increíbles 2', 'estudio': 'Walt Disney Pictures', 'año': 2018},
    {'titulo': 'Avengers: Infinity War', 'estudio': 'Marvel Studios', 'año': 2018},
    {'titulo': 'Capitán América: Civil War', 'estudio': 'Marvel Studios', 'año': 2016},
    {'titulo': 'Deadpool', 'estudio': 'Marvel Studios', 'año': 2016},
]

pila_peliculas = Pila()

for pelicula in peliculas:
    pila_peliculas.push(pelicula)


print("Películas estrenadas en 2014:")
while pila_peliculas.size() > 0:
    pelicula = pila_peliculas.pop()
    if pelicula['año'] == 2014:
        print(pelicula['titulo'])


for pelicula in peliculas:
    pila_peliculas.push(pelicula)

contador_2018 = 0
while pila_peliculas.size() > 0:
    pelicula = pila_peliculas.pop()
    if pelicula['año'] == 2018:
        contador_2018 += 1
print("Número de películas estrenadas en 2018:", contador_2018)


for pelicula in peliculas:
    pila_peliculas.push(pelicula)


print("Películas de Marvel Studios estrenadas en 2016:")
while pila_peliculas.size() > 0:
    pelicula = pila_peliculas.pop()
    if pelicula['estudio'] == 'Marvel Studios' and pelicula['año'] == 2016:
        print(pelicula['titulo'])







