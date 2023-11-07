from arbol_binario import BinaryTree
'''Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenadade los cuales se conoce su name, número, type/types para el cual debemos construir tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente: 
a) los índices de cada uno de los árboles deben ser name, número y type; 
b) mostrar todos los datos de un Pokémon a partir de su número y name –para este
último, la búsqueda debe ser por proximidad, 
es decir si busco “bul” se deben mostrar todos los Pokémons cuyos 
names comiencen o contengan dichos caracteres–; 
c) mostrar todos los names de todos los Pokémons de un determinado type agua, fuego, planta y eléctrico; 
d) realizar un listado en orden ascendente por número y name de Pokémon, y además un listado por nivel por name; 
e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
f) Determina cuantos Pokémons hay de type eléctrico y acero.'''


treeName = BinaryTree()
treeNumero = BinaryTree()
treeTipo = BinaryTree()

# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
pokemon_data = [
    {'name':"Bulbasaur", 'numero':1, 'tipo': "Planta - Veneno"},
    {'name':"Charmander", 'numero':4, 'tipo':"Fuego"},
    {'name':"Squirtle", 'numero':7, 'tipo':"Agua"},
    {'name':"Pikachu", 'numero':25, 'tipo':"Eléctrico"},
    {'name':"Jigglypuff", 'numero':39,'tipo': "Normal - Hada"},
    {'name':"Gengar", 'numero':94, 'tipo':"Fantasma - Veneno"},
    {'name':"Snorlax", 'numero':143, 'tipo':"Normal"},
    {'name':"Mewtwo", 'numero':150, 'tipo':"Psíquico"},
    {'name':"Gyarados", 'numero':130, 'tipo':"Agua - Volador"},
    {'name':"Machamp", 'numero':68, 'tipo':"Lucha"},
    {'name':"Jolteon", 'numero':135, 'tipo':"Eléctrico"},
    {'name':"Lycanroc", 'numero':745, 'tipo':"Roca"},
    {'name':"Tyrantrum", 'numero':697, 'tipo':"Roca - Dragón"},
    {'name':"Lucario", 'numero':448, 'tipo':"Acero"}]

for i in pokemon_data:
    treeName.insert_node(i['name'], [i['numero'], i['tipo']])
    treeNumero.insert_node(i['numero'], [i['name'], i['tipo']])
    treeTipo.insert_node(i['tipo'], i['name'], i['numero'])
print('------------------------------------------------------------------------------')
print('Pokemons por nombre:')
treeName.postorden()
print('------------------------------------------------------------------------------')
print('Pokemons por numero:')
treeNumero.postorden()
treeTipo.postorden()

# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–


treeName.search_by_coincidence_with_proximi('Pik')
treeNumero.search_Number_Pokemons(4)

# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
print('------------------------------------------------------------------------------')
print('Pokemons tipo agua, fuego, planta y eléctrico;')
treeTipo.inorden_Tipos()


# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
print('------------------------------------------------------------------------------')
print('Realizar un listado en orden ascendente por número y nombre de Pokémon y además un listado por nivel por nombre')
print('inorden nombre')
treeName.inordenName()
print()
print('inorden numero')
treeNumero.inordenNumero()
print()
print('by level nombre')
treeName.by_level_name()

# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
print('------------------------------------------------------------------------------')
print('Mostrar datos de los pokemones Jolteon, Lycanroc y Tyrantrum')
value1 = treeName.search("Jolteon")
print(f"Nombre: {value1.value}. Numero: {value1.other_values[0]}. Tipo: {value1.other_values[1]}")

value2 = treeName.search("Lycanroc")
print(f"Nombre: {value2.value}. Numero: {value2.other_values[0]}. Tipo: {value2.other_values[1]}")

value3 = treeName.search("Tyrantrum")
print(f"Nombre: {value3.value}. Numero: {value3.other_values[0]}. Tipo: {value3.other_values[1]}")

print('------------------------------------------------------------------------------')
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.
electricosHay = treeTipo.contarElectricos()
print('Hay', electricosHay, 'Pokemons Electricos')
acerosHay = treeTipo.contarAcero()
print('Hay', acerosHay, 'Pokemons de Acero')

