'''Dada una lista con nombres de personajes de la saga de Avengers
ordenados por nombre del superhéroes, de los cuales se conoce:
nombre del superhéroe, nombre del personaje (puede ser vacio),
grupo al que (perteneces puede ser vacio), año de aparición, por
ejemplo (Star Lord , Peter Quill , Guardianes de la galaxia - 1976).
Resolver las siguientes tareas:
a. Determinar si “Capitana Marvel” está en la lista y mostrar su
nombre de personaje;
b. Almacenar los superhéroes que pertenezcan al grupo
“Guardianes de la galaxia” en una cola e indicar cuantos son.
c. Mostrar de manera descendente los superhéroes que
pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de
la galaxia”.
d. Listar los superhéroes que tengan nombre de personajes cuyo
año de aparición sea posterior a 1960.
e. Hemos detectado que la superhéroe “Black Widow” está mal
cargada por un error de tipeo, figura como “Vlanck Widow”,
modifique dicho superhéroe para solucionar este problema.
f. Dada una lista auxiliar con los siguientes personajes ("Black
Cat", "Hulk", "Rocket Racoonn", "Loki", complete el resto de la
información), agregarlos a la lista principal en el caso de no
estar cargados.
g. Mostrar todos los personajes que comienzan con C, P o S.
h. Cargue al menos 20 superheroes a la lista.'''

from collections import deque

def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            return ''


class Lista():

    def __init__(self):
        self.__elements = []

    def insert(self, value, criterio=None):
        if len(self.__elements) == 0:
            self.__elements.append(value)
        else:
            index = 0
            while index < len(self.__elements) and (
                    criterio_comparacion(value, criterio) is not None and criterio_comparacion(self.__elements[index],
                                                                                              criterio) is not None and
                    criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index], criterio)):
                index += 1
            self.__elements.insert(index, value)

    def search(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.size() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

    def search_r(self, search_value, first, last, criterio=None):
        middle = (first + last) // 2
        if first > last:
            return None
        elif search_value == criterio_comparacion(self.__elements[middle], criterio):
            return middle
        elif search_value > criterio_comparacion(self.__elements[middle], criterio):
            return self.search_r(search_value, middle + 1, last, criterio)
        else:
            return self.search_r(search_value, first, middle - 1, criterio)


    def delete(self, value, criterio=None):
        return_value = None
        pos = self.search(value, criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
        return return_value

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value)

    def order_by(self, criterio=None, reverse=False):
        def func_criterio(valor):
            return criterio_comparacion(valor, criterio)

        self.__elements.sort(key=func_criterio, reverse=reverse)

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value

    def set_value(self, value, new_value, criterio=None):
        pos = self.search(value, criterio)
        if pos is not None:
            value = self.delete(value)
            self.insert(new_value, criterio)


class Personaje:
    def __init__(self, nombre_superheroe, nombre_personaje, grupo, anio_aparicion):
        self.nombre_superheroe = nombre_superheroe
        self.nombre_personaje = nombre_personaje
        self.grupo = grupo
        self.anio_aparicion = anio_aparicion
    
    def __repr__(self):
        return f"Nombre Superheroe: {self.nombre_superheroe}, Nombre Pila: {self.nombre_personaje}, Grupo al que pertenece: {self.grupo}, Año de apariccion: {self.anio_aparicion}"


lista_avengers = Lista()
lista_avengers.insert(Personaje("Capitana Marvel", "Carol Danvers", "Avengers", 1968))
lista_avengers.insert(Personaje("Capitán America", "Steve Rogers", "Avengers", 1941))
lista_avengers.insert(Personaje("Iron Man", "Tony Stark", "Avengers", 1963))
lista_avengers.insert(Personaje("Thor", "", "Avengers", 1962))
lista_avengers.insert(Personaje("Vlanck Widow", "Natasha Romanoff", "Avengers", 1964))
lista_avengers.insert(Personaje("Ojo de Halcón", "Clint Barton", "Avengers", 1964))
lista_avengers.insert(Personaje("Bruja Escarlata", "Wanda Maximoff", "Avengers", 1964))
lista_avengers.insert(Personaje("Visión", "", "Avengers", 1968))
lista_avengers.insert(Personaje("Doctor Strange", "Stephen Strange", "Avengers", 1963))
lista_avengers.insert(Personaje("Pantera Negra", "T'Challa", "Avengers", 1966))
lista_avengers.insert(Personaje("Patriot", "Elijah Bradley", "Avengers", 2001))
lista_avengers.insert(Personaje("Star Lord", "Peter Quill", "Guardianes de la Galaxia", 1976))
lista_avengers.insert(Personaje("Gamora", "", "Guardianes de la Galaxia", 1975))
lista_avengers.insert(Personaje("Rocket Raccoon", "", "Guardianes de la Galaxia", 1976))
lista_avengers.insert(Personaje("Groot", "", "Guardianes de la Galaxia", 1960))
lista_avengers.insert(Personaje("Sr. Fantástico", "Reed Richards", "Los Cuatro Fantásticos", 1961))
lista_avengers.insert(Personaje("Mujer Invisible", "Sue Storm", "Los Cuatro Fantásticos", 1961))
lista_avengers.insert(Personaje("Antorcha Humana", "Johnny Storm", "Los Cuatro Fantásticos", 1961))
lista_avengers.insert(Personaje("Spider-Man", "Peter Parker", "Avengers", 1962))
lista_avengers.insert(Personaje("Scarlet Witch", "Wanda Maximoff", "Avengers", 1964))

print('------------------------------------------------------------------------------------')

#! Determinar si "Capitana Marvel" está en la lista y mostrar su nombre de personaje
capitana_marvel_posicion = lista_avengers.search("Capitana Marvel", "nombre_superheroe")
if capitana_marvel_posicion is not None:
    capitana_marvel = lista_avengers.get_element_by_index(capitana_marvel_posicion)
    if capitana_marvel is not None:
        print("Nombre de personaje de Capitana Marvel:", capitana_marvel.nombre_personaje)
    
print('------------------------------------------------------------------------------------')

#! b. Almacenar los superhéroes que pertenezcan al grupo “Guardianes de la galaxia” en una cola e indicar cuantos son.
print('Guardianes de la Galaxia:')
cola_guardianes = deque()
for personaje in lista_avengers._Lista__elements:
    if personaje.grupo == "Guardianes de la Galaxia":
        cola_guardianes.append(personaje)
cantidad_guardianes = len(cola_guardianes)
print("La cantidad de superhéroes del grupo 'Guardianes de la Galaxia' es:", cantidad_guardianes)

print('------------------------------------------------------------------------------------')

#! c. Mostrar de manera descendente los superhéroes que pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de la galaxia”.
print('Personajes pertenecientes a "Los Cutro fantasticos", y "Guardianes de la Galxia", de manera decendiente:')
superheroes = []
for personaje in lista_avengers._Lista__elements:
    if personaje.grupo == "Los Cuatro Fantásticos" or personaje.grupo == "Guardianes de la Galaxia":
        superheroes.append(personaje)
for personaje in superheroes:
    print(personaje)
    
print('------------------------------------------------------------------------------------')

#! d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960.
print('Personajes cuyo año de apariccion fue posterior a 1960:')
for personaje in lista_avengers._Lista__elements:
    if personaje.anio_aparicion > 1960:
        print(f"Año: {personaje.anio_aparicion}, Nombre: {personaje.nombre_superheroe}")
        
print('------------------------------------------------------------------------------------')

#! e. Hemos detectado que la superhéroe “Black Widow” está mal cargada por un error de tipeo, figura como “Vlanck Widow”, modifique dicho superhéroe para solucionar este problema.
print('Personaje Corregido:')
for i in range(lista_avengers.size()):
    personaje = lista_avengers.get_element_by_index(i)
    if personaje.nombre_superheroe == "Vlanck Widow":
        personaje.nombre_superheroe = "Black Widow"
        print(personaje)
        break
    
print('------------------------------------------------------------------------------------')

#! f. Dada una lista auxiliar con los siguientes personajes (‘Black Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la información), agregarlos a la lista principal en el caso de no estar cargados.
print('Se imprimira la Lista con los nuevos Superheroes:')
auxiliary_list = [
    Personaje("Black Cat", "Felicia Hardy", "Avengers", 1979),
    Personaje("Hulk", "Bruce Banner", "Avengers", 1962),
    Personaje("Rocket Racoonn", "Rocket", "Avengers", 1976),
    Personaje("Loki", "Loki Laufeyson", "Avengers", 1949)
]
for character in auxiliary_list:
    if lista_avengers.search(character.nombre_personaje) is None:
        lista_avengers.insert(character)
lista_avengers.barrido()

print('------------------------------------------------------------------------------------')

#! g. Mostrar todos los personajes que comienzan con C, P o S.
print('Nombres de personajes que comiencen por C, P o S:')
def mostrar_nombres_personajes(lista, letras):
    for i in range(lista.size()):
        personaje = lista.get_element_by_index(i)
        if personaje.nombre_superheroe[0] in letras:
            print(personaje.nombre_superheroe)
letras_iniciales = ['C', 'P', 'S']
mostrar_nombres_personajes(lista_avengers, letras_iniciales)

print('------------------------------------------------------------------------------------')

#! h. Cargue al menos 20 superheroes a la lista.
cantidad_superheroes = lista_avengers.size()
print("Cantidad de superhéroes en la lista:", cantidad_superheroes)

print('------------------------------------------------------------------------------------')
