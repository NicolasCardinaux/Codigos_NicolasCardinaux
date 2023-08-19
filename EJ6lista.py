'''Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
rias para poder realizar las siguientes actividades:

a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic.'''
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
 
    def delete(self, value_name):
     pos = self.search(value_name, "nombre")
     if pos is not None:
        return_value = self.__elements.pop(pos)
     return return_value


    def size(self):
        return len(self.__elements)

   
    def barrido(self):
     for value in self.__elements:
        print(f"Nombre: {value.nombre}, Año: {value.año_creacion}, Casa: {value.editorial}, Biografía: {value.descripcion}")


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

    def set_value(self, old_value, new_value, criterio=None):
     pos = self.search(old_value.nombre, "nombre")
     if pos is not None:
        self.delete(old_value.nombre, "nombre")
        self.insert(new_value, criterio)


            
class Superheroe:
    def __init__(self, nombre, año_creacion, editorial, descripcion):
        self.nombre = nombre
        self.año_creacion = año_creacion
        self.editorial = editorial
        self.descripcion = descripcion

lista_superheroes = [
    Superheroe("Superman", 1938, "DC", "Superman es un superhéroe conocido por su increíble fuerza y capacidad de volar."),
    Superheroe("Spider-Man", 1962, "Marvel", "Spider-Man es un superhéroe conocido por sus habilidades arácnidas y su traje."),
    Superheroe("Capitana Marvel", 1968, "Marvel", "Capitana Marvel es Carol Danvers, una piloto de la Fuerza Aérea que obtiene poderes cósmicos y se convierte en una poderosa heroína."),
    Superheroe("Batman", 1939, "DC", "Batman es un superhéroe que lucha contra el crimen en Gotham City, usando su intelecto y gadgets."),
    Superheroe("Wolverine", 1974, "Marvel", "Wolverine es un superhéroe con un esqueleto de adamantium y garras retráctiles, siendo prácticamente inmortal."),
    Superheroe("Linterna Verde", 1940, "DC", "Linterna Verde es un superhéroe miembro de los Green Lantern Corps, con un anillo que le otorga poderes sobrenaturales."),
    Superheroe("Dr. Strange", 1963, "DC", "Dr. Strange es un superhéroe maestro de las artes místicas, capaz de manipular la realidad y luchar contra amenazas sobrenaturales."),
    Superheroe("Mujer Maravilla", 1941, "DC", "Mujer Maravilla es una guerrera amazona con fuerza sobrehumana y portadora de los dones de los dioses."),
    Superheroe("Flash", 1940, "DC", "Flash es un velocista con la habilidad de correr a velocidades increíbles, siendo el ser más rápido del universo."),
    Superheroe("Star-Lord", 1976, "Marvel", "Star-Lord es Peter Quill, un aventurero espacial que lidera a los Guardianes de la Galaxia en su lucha contra amenazas cósmicas."),
    Superheroe("Iron Man", 1963, "Marvel", "Iron Man es Tony Stark, un genio, multimillonario y filántropo que construye una armadura tecnológica para combatir el crimen."),
    Superheroe("Black Widow", 1964, "Marvel", "Black Widow es Natasha Romanoff, una espía y asesina entrenada que se convierte en una valiosa miembro de los Vengadores."),
    Superheroe("Aquaman", 1941, "DC", "Aquaman es el rey de la Atlántida y tiene la capacidad de comunicarse y controlar a los seres marinos.")
]
superheroes_lista = Lista()
for heroe in lista_superheroes:
    superheroes_lista.insert(heroe, "nombre")

print('----------------------------------------------------------------------------')

#a. Eliminar el nodo que contiene la información de Linterna Verde
superheroes_lista.delete("Linterna Verde")
linterna_verde_search = superheroes_lista.search("Linterna Verde", "nombre")
if linterna_verde_search is None:
    print("Linterna Verde fue eliminado correctamente.")
else:
    print("Linterna Verde no se eliminó correctamente.")

print('----------------------------------------------------------------------------')

# b. Mostrar el año de aparición de Wolverine
wolverine = Superheroe("Wolverine", None, None, None)
pos_wolverine = superheroes_lista.search(wolverine.nombre, "nombre")
if pos_wolverine is not None:
    print(f"Año de aparición de Wolverine: {superheroes_lista.get_element_by_index(pos_wolverine).año_creacion}")

print('----------------------------------------------------------------------------')

# c. Cambiar la casa de Dr. Strange a Marvel
pos_dr_strange = superheroes_lista.search("Dr. Strange", "nombre")
if pos_dr_strange is not None:
    dr_strange_instance = superheroes_lista.get_element_by_index(pos_dr_strange)
    dr_strange_instance.editorial = "Marvel"
    print(f"La nueva editorial de Dr. Strange es: {dr_strange_instance.editorial}")

print('----------------------------------------------------------------------------')

# d. Mostrar el nombre de superhéroes con "traje" o "armadura" en su biografía
print("Superhéroes con 'traje' o 'armadura' en su biografía:")
for heroe in lista_superheroes:
    if "traje" in heroe.descripcion.lower() or "armadura" in heroe.descripcion.lower():
        print(heroe.nombre)

print('----------------------------------------------------------------------------')

# e. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición es anterior a 1963
print("Superhéroes cuya fecha de aparición es anterior a 1963:")
for heroe in lista_superheroes:
    if heroe.año_creacion < 1963:
        print(f"Nombre: {heroe.nombre}, Casa: {heroe.editorial}")

print('----------------------------------------------------------------------------')

# f. Mostrar la casa de Capitana Marvel y Mujer Maravilla
print("Casa de Capitana Marvel y Mujer Maravilla:")
for heroe in lista_superheroes:
    if heroe.nombre == "Capitana Marvel" or heroe.nombre == "Mujer Maravilla":
        print(f"Nombre: {heroe.nombre}, Casa: {heroe.editorial}")

print('----------------------------------------------------------------------------')


# g. Mostrar toda la información de Flash y Star-Lord
print("Información de Flash y Star-Lord:")
for heroe in lista_superheroes:
    if heroe.nombre == "Flash" or heroe.nombre == "Star-Lord":
        print(f"Nombre: {heroe.nombre}")
        print(f"Año de aparición: {heroe.año_creacion}")
        print(f"Casa de cómic: {heroe.editorial}")
        print(f"Biografía: {heroe.descripcion}\n")


print('----------------------------------------------------------------------------')

# h. Listar superhéroes que comienzan con B, M y S
print("Superhéroes que comienzan con B, M y S:")
for heroe in lista_superheroes:
    if heroe.nombre[0] in ['B', 'M', 'S']:
        print(heroe.nombre)

print('----------------------------------------------------------------------------')


# i. Determinar cuántos superhéroes hay de cada casa de comic
contador_dc = 0
contador_marvel = 0
for heroe in lista_superheroes:
    if heroe.editorial == "DC":
        contador_dc += 1
    elif heroe.editorial == "Marvel":
        contador_marvel += 1
print(f"Número de superhéroes de DC: {contador_dc}")
print(f"Número de superhéroes de Marvel: {contador_marvel}")

print('----------------------------------------------------------------------------')

