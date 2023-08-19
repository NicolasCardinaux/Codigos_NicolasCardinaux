from random import randint

class ListaSimple():

    def __init__(self):
        self.__elements = []

    def insert(self, value, criterio=None):
        # print('criterio de insercion', criterio)
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1], criterio):
            self.__elements.append(value)
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0], criterio):
            self.__elements.insert(0, value)
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index], criterio):
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
            return self.search_r(search_value, middle+1, last, criterio)
        else:
            return self.search_r(search_value, first, middle-1, criterio)
 
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
        dic_atributos = self.__elements[0].__dict__
        if criterio in dic_atributos:
            def func_criterio(valor):
                return valor.__dict__[criterio]

            self.__elements.sort(key=func_criterio, reverse=reverse)
        else:
            print('no se puede ordenar por este criterio')

   
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

def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')


class Lista():

    def __init__(self):
        self.__elements = []

    def insert(self, value, criterio=None):
        # print('criterio de insercion', criterio)
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1][0], criterio):
            self.__elements.append([value, ListaSimple()])
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0][0], criterio):
            self.__elements.insert(0, [value, ListaSimple()])
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index][0], criterio):
                index += 1
            self.__elements.insert(index, [value, ListaSimple()])

    def search(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.size() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle][0], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle][0], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

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
            print(value[0])
            print('Sublista ----------------')
            value[1].barrido()

    def barrido_entrenadores(self):
        for value in self.__elements:
            print(value[0])
            print('Lista de Pokemons:')
            value[1].barrido()
            print()
            
    def obtener_pokemons_especiales(self, entrenador_info):
        pokemons_especiales = []
        sublista = entrenador_info[1]
        for pos in range(sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            if (pokemon.tipo == 'fuego' and pokemon.subtipo == 'planta') or (pokemon.tipo == 'agua' and pokemon.subtipo == 'volador'):
                pokemons_especiales.append(pokemon)
        return pokemons_especiales
            
    def barrido_cantidad_batallas_ganadas(self, cantidad_batallas):
        for value in self.__elements:
            if value[0].cb_ganadas >= cantidad_batallas:
                print(f'{value[0].nombre} ha ganado {value[0].cb_ganadas} batallas')

    def barrido_cantidad_torneos_ganados(self, cantidad_victorias):
        for value in self.__elements:
            if value[0].ct_ganados > cantidad_victorias:
                print(f'{value[0].nombre} ha ganado {value[0].ct_ganados} torneos')

    def order_by(self, criterio=None, reverse=False):
        dic_atributos = self.__elements[0][0].__dict__
        if criterio in dic_atributos:
            def func_criterio(valor):
                return valor.__dict__[criterio]

            self.__elements.sort(key=func_criterio, reverse=reverse)
        else:
            print('no se puede ordenar por este criterio')

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value



'''Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas.
Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo.
Se pide resolver
las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;
c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;
j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos;'''


class Entrenador():

    def __init__(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} --> Cantidad de torneos ganadas:{self.ct_ganados}-Cantidad de batallas ganadas {self.cb_ganadas}- Cantidad de batallas perdidas{self.cb_perdidas}'

class Pokemon():

    def __init__(self, nombre, nivel,  tipo, subtipo=None):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}'


e1 = Entrenador('Juan', 1, 3, 5)
e2 = Entrenador('Maria', 1, 4, 3)
e3 = Entrenador('Ana', 1, 5, 1)
e4 = Entrenador('Carlos', 5, 3, 10)
e5 = Entrenador('Luisa', 2, 6, 6)
e6 = Entrenador('Pedro', 0, 3, 2)
e7 = Entrenador('Sofía', 4, 5, 9)
e8 = Entrenador('Andrés', 2, 5, 4)
e9 = Entrenador('Laura', 3, 7, 8)
e10 = Entrenador('Miguel', 1, 2, 2)

entrenadores = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]

lista_entrenadores = Lista()

p1 = Pokemon('pikachu', 3, 'fuego', 'planta')
p2 = Pokemon('bulbasaur', 5, 'planta', 'veneno')
p3 = Pokemon('charmander', 2, 'fuego', 'tierra')
p4 = Pokemon('Wingull', 4, 'agua', 'cielo')
p5 = Pokemon('eevee', 3, 'normal', 'tierra')
p6 = Pokemon('Tyrantrum', 1, 'volador', 'hada')
p7 = Pokemon('geodude', 6, 'roca', 'tierra')
p8 = Pokemon('machop', 3, 'agua', 'volador')
p9 = Pokemon('Terrakion', 2, 'psíquico', 'telepatico')
p10 = Pokemon('caterpie', 1, 'planta', 'bosque')
p11 = Pokemon('pikachu', 1, 'fuego', 'planta')
p12 = Pokemon('eevee', 5, 'normal', 'tierra')
p13 = Pokemon('geodude', 4, 'roca', 'tierra')

pokemons = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13]

#! lista principal
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

#! lista secundaria
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')

print('----------------------------------------------------------------------------')

#! A. obtener la cantidad de Pokémons de un determinado entrenador;
print( 'Obtener la cantidad de Pokémons de un determinado entrenador')
nombre_entrenador = 'Pedro' 
pos = lista_entrenadores.search(nombre_entrenador, 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} Pokémon')


print('----------------------------------------------------------------------------')

#! B. Listar los entrenadores que hayan ganado más de tres torneos
print('Listar los entrenadores que hayan ganado más de tres torneos')
print()
lista_entrenadores.barrido_cantidad_torneos_ganados(3)


print('----------------------------------------------------------------------------')

#!# C. Encontrar el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
print('Encontrar el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados')
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
pos_mayor = 0

for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.ct_ganados
        
valor = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = valor[0], valor[1]

pokemon_mayor = sublista.get_element_by_index(0)

for pos in range(1, sublista.size()):
    pokemon = sublista.get_element_by_index(pos)
    if pokemon.nivel > pokemon_mayor.nivel:
        pokemon_mayor = pokemon

if pokemon_mayor is not None:
    nivel_pokemon_mayor = pokemon_mayor.nivel
    if hasattr(pokemon_mayor, 'nombre'):
        nombre_pokemon_mayor = pokemon_mayor.nombre
    else:
        nombre_pokemon_mayor = 'desconocido'
    print(f'El Pokémon de mayor nivel del entrenador {entrenador.nombre} es {nombre_pokemon_mayor} (Nivel {nivel_pokemon_mayor})')
else:
    print(f'El entrenador {entrenador.nombre} no tiene Pokémons en su sublista')
    
print('----------------------------------------------------------------------------')


#! D. mostrar todos los datos de un entrenador y sus Pokémos;
print("\nDatos de un entrenador y sus Pokémon aleatorio:")
index_aleatorio = randint(0, lista_entrenadores.size() - 1)
entrenador_info = lista_entrenadores.get_element_by_index(index_aleatorio)
entrenador = entrenador_info[0]
sublista = entrenador_info[1]

print("Entrenador:")
print(f"Nombre: {entrenador.nombre}")
print(f"Tormentos ganados: {entrenador.ct_ganados}")
print(f"Batallas ganadas: {entrenador.cb_ganadas}")
print(f"Batallas perdidas: {entrenador.cb_perdidas}")

if sublista.size() > 0:
    print("\nPokémon:")
    sublista.barrido()
else:
    print("Este entrenador no tiene Pokémons en su sublista.")
    
print('----------------------------------------------------------------------------')

#!E. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print("Entrenadores con más del 79% de batallas ganadas (10 es 100%):")
lista_entrenadores.barrido_cantidad_batallas_ganadas(8)

print('----------------------------------------------------------------------------')

#! f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
print("\nEntrenadores con Pokémon de tipo fuego y planta, o agua/volador:")
for pos in range(lista_entrenadores.size()):
    entrenador_info = lista_entrenadores.get_element_by_index(pos)
    entrenador = entrenador_info[0]
    pokemons_especiales = lista_entrenadores.obtener_pokemons_especiales(entrenador_info)

    if pokemons_especiales:
        print(f"{entrenador.nombre} tiene los siguientes Pokémon especiales:")
        for pokemon in pokemons_especiales:
            print(f"   - {pokemon.nombre}")
            
print('----------------------------------------------------------------------------')

#!g. el promedio de nivel de los Pokémons de un determinado entrenador;
print('El promedio de nivel de los Pokémons de un determinado entrenador')
nombre_entrenador = 'Juan'  
pos = lista_entrenadores.search(nombre_entrenador, 'nombre')

if pos is not None:
    entrenador_info = lista_entrenadores.get_element_by_index(pos)
    entrenador = entrenador_info[0]
    sublista = entrenador_info[1]
    total_niveles = 0
    cantidad_pokemons = sublista.size()

    for pos_pokemon in range(cantidad_pokemons):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        total_niveles += pokemon.nivel

    if cantidad_pokemons > 0:
        promedio_nivel = total_niveles / cantidad_pokemons
        print(f"El promedio de nivel de los Pokémon de {entrenador.nombre} es {promedio_nivel:.2f}")
    else:
        print(f"{entrenador.nombre} no tiene Pokémon en su sublista.")
else:
    print(f"No se encontró un entrenador con el nombre {nombre_entrenador}")
    
print('----------------------------------------------------------------------------')

#!h. determinar cuántos entrenadores tienen a un determinado Pokémon;
print('Determinar cuántos entrenadores tienen a un determinado Pokémon')
nombre_pokemon_buscar = 'pikachu'  
cantidad_entrenadores = 0

for pos_entrenador in range(lista_entrenadores.size()):
    entrenador_info = lista_entrenadores.get_element_by_index(pos_entrenador)
    sublista = entrenador_info[1]
    
    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        if pokemon.nombre.lower() == nombre_pokemon_buscar.lower():
            cantidad_entrenadores += 1
            break  

if cantidad_entrenadores > 0:
    print(f"{cantidad_entrenadores} entrenadores tienen al Pokémon {nombre_pokemon_buscar}.")
else:
    print(f"Ningún entrenador tiene al Pokémon {nombre_pokemon_buscar}.")
    
print('----------------------------------------------------------------------------')


#!i. mostrar los entrenadores que tienen Pokémons repetidos;
entrenadores_con_repetidos = []

for pos_entrenador in range(lista_entrenadores.size()):
    entrenador_info = lista_entrenadores.get_element_by_index(pos_entrenador)
    sublista = entrenador_info[1]
    pokemons_vistos = set()
    pokemons_repetidos = []
    
    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        if pokemon.nombre.lower() in pokemons_vistos:
            pokemons_repetidos.append(pokemon.nombre)
        pokemons_vistos.add(pokemon.nombre.lower())
    
    if pokemons_repetidos:
        entrenadores_con_repetidos.append((entrenador_info[0], pokemons_repetidos))

if entrenadores_con_repetidos:
    print("Los siguientes entrenadores tienen Pokémon repetidos:")
    for entrenador, pokemons_repetidos in entrenadores_con_repetidos:
        print(f"   - {entrenador.nombre}: {', '.join(pokemons_repetidos)}")
else:
    print("Ningún entrenador tiene Pokémon repetidos en su sublista.")
    
print('----------------------------------------------------------------------------')

#! j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
pokemons_buscar = ['Tyrantrum', 'Terrakion', 'Wingull']
entrenadores_con_pokemons_especificos = []

for pos_entrenador in range(lista_entrenadores.size()):
    entrenador_info = lista_entrenadores.get_element_by_index(pos_entrenador)
    sublista = entrenador_info[1]
    pokemons_especificos = []
    
    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        if pokemon.nombre in pokemons_buscar:
            pokemons_especificos.append(pokemon.nombre)
    
    if pokemons_especificos:
        entrenadores_con_pokemons_especificos.append((entrenador_info[0], pokemons_especificos))

if entrenadores_con_pokemons_especificos:
    print("Los siguientes entrenadores tienen uno de los siguientes Pokémons (Tyrantrum, Terrakion o Wingull):")
    for entrenador, pokemons_especificos in entrenadores_con_pokemons_especificos:
        pokemon_str = ', '.join(pokemons_especificos)
        print(f"   - {entrenador.nombre}: {pokemon_str}")
else:
    print("Ningún entrenador tiene ninguno de los Pokémons especificados.")
    
print('----------------------------------------------------------------------------')

#!k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#!como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
#!deberán mostrar los datos de ambos
print('Determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos')
nombre_entrenador_buscar = 'Ana'  
nombre_pokemon_buscar = 'pikachu'  

pos_entrenador = lista_entrenadores.search(nombre_entrenador_buscar, 'nombre')
entrenador_encontrado = None
pokemon_encontrado = None

if pos_entrenador is not None:
    entrenador_encontrado = lista_entrenadores.get_element_by_index(pos_entrenador)[0]
    sublista = lista_entrenadores.get_element_by_index(pos_entrenador)[1]
    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        if pokemon.nombre.lower() == nombre_pokemon_buscar.lower():
            pokemon_encontrado = pokemon
            break

if entrenador_encontrado is not None and pokemon_encontrado is not None:
    print(f"El entrenador {entrenador_encontrado.nombre} tiene al Pokémon {nombre_pokemon_buscar}:")
    print(f"Entrenador:")
    print(f"Nombre: {entrenador_encontrado.nombre}")
    print(f"Tormentos ganados: {entrenador_encontrado.ct_ganados}")
    print(f"Batallas ganadas: {entrenador_encontrado.cb_ganadas}")
    print(f"Batallas perdidas: {entrenador_encontrado.cb_perdidas}")
    print(f"\nPokémon:")
    print(f"Nombre: {pokemon_encontrado.nombre}")
    print(f"Nivel: {pokemon_encontrado.nivel}")
    print(f"Tipo: {pokemon_encontrado.tipo}")
    if hasattr(pokemon_encontrado, 'subtipo'):
        print(f"Subtipo: {pokemon_encontrado.subtipo}")
else:
    print(f"El entrenador {nombre_entrenador_buscar} no tiene al Pokémon {nombre_pokemon_buscar}.")










