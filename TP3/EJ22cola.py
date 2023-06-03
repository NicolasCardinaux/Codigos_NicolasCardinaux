'''Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino

F) -por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
de superhéroes.'''
class Cola:
    def __init__(self):
        self.__elementos = []

    def arrive(self, value):
        self.__elementos.append(value)

    def atencion(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):
        return len(self.__elementos)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atencion()
            self.arrive(aux)
            return aux
        
    def __repr__(self):
        return f"Cola: {self.__elementos}"
        
    
class Super:
    def __init__(self, nom, nomsup, sex):
        self.nom = nom
        self.nomsup = nomsup
        self.sex = sex

    def __repr__(self):
        return f"Nombre: {self.nom}, Nombre de Superheroe: {self.nomsup}, Genero: {self.sex}\n"

cola_personajes = Cola()
cola_personajes.arrive(Super('Tony Stark', "Iron Man", "M"))
cola_personajes.arrive(Super('Steve Rogers', 'Capitán América', 'M'))
cola_personajes.arrive(Super('Natasha Romanoff', 'Viuda Negra', 'F'))
cola_personajes.arrive(Super('Bruce Banner', 'Hulk', 'M'))
cola_personajes.arrive(Super('Thor Odinson', 'Thor', 'M'))
cola_personajes.arrive(Super('Peter Parker', 'Spider-Man', 'M'))
cola_personajes.arrive(Super('Stephen Strange', 'Doctor Strange', 'M'))
cola_personajes.arrive(Super('Scott Lang', 'Ant-Man', 'M'))
cola_personajes.arrive(Super('Carol Danvers', 'Capitana Marvel', 'F'))
cola_personajes.arrive(Super('Sam Wilson', 'Falcon', 'M'))

print('----------------------------------------------------------------------------')

#! a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
def find_character_by_superhero(cola, superhero):
    for personaje in cola._Cola__elementos:
        if personaje.nomsup == superhero:
            return personaje.nom
    return None

nombre_capitana_marvel = find_character_by_superhero(cola_personajes, "Capitana Marvel")
print("Nombre del personaje de la Capitana Marvel:", nombre_capitana_marvel)

print('----------------------------------------------------------------------------')

#! b. Mostrar los nombres de los superhéroes femeninos
superheroes_femeninos = [personaje.nomsup for personaje in cola_personajes._Cola__elementos if personaje.sex == "F"]
print("Nombres de los superhéroes femeninos:", superheroes_femeninos)

print('----------------------------------------------------------------------------')

#! c. Mostrar los nombres de los personajes masculinos
personajes_masculinos = [personaje.nom for personaje in cola_personajes._Cola__elementos if personaje.sex == "M"]
print("Nombres de los personajes masculinos:", personajes_masculinos)

print('----------------------------------------------------------------------------')

#! d. Determinar el nombre del superhéroe del personaje Scott Lang
def find_superhero_by_character(cola, character):
    for personaje in cola._Cola__elementos:
        if personaje.nom == character:
            return personaje.nomsup
    return None

nombre_superheroe_scott_lang = find_superhero_by_character(cola_personajes, "Scott Lang")
print("Nombre del superhéroe del personaje Scott Lang:", nombre_superheroe_scott_lang)

print('----------------------------------------------------------------------------')

#! e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
personajes_con_s = [personaje for personaje in cola_personajes._Cola__elementos if personaje.nom.startswith("S")]
print("Datos de los superhéroes o personajes cuyos nombres comienzan con la letra S:")
for personaje in personajes_con_s:
    print(personaje)
    
print('----------------------------------------------------------------------------')

#! f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
def find_character_by_name(cola, character_name):
    for personaje in cola._Cola__elementos:
        if personaje.nom == character_name:
            return personaje.nomsup
    return None

nombre_superheroe_carol_danvers = find_character_by_name(cola_personajes, "Carol Danvers")
if nombre_superheroe_carol_danvers is not None:
    print("El personaje Carol Danvers se encuentra en la cola. Su nombre de superhéroe es:", nombre_superheroe_carol_danvers)
else:
    print("El personaje Carol Danvers no se encuentra en la cola.")

print('----------------------------------------------------------------------------')