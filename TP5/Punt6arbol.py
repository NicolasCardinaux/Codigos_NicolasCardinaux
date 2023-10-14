from arbolbinario import BinaryTree, get_value_from_file
ruta_del_archivo = r'C:\Users\nicoc\OneDrive\Escritorio\Python_facultad\arbol\jedis.txt'

'''Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de naci-
miento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
siguientes consignas:
a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
b. realizar un barrido inorden del árbol por nombre y ranking;
c. realizar un barrido por nivel de los árboles por ranking y especie;
d. mostrar toda la información de Yoda y Luke Skywalker;
e. mostrar todos los Jedi con ranking “Jedi Master”;
f. listar todos los Jedi que utilizaron sabe de luz color verde;
g. listar todos los Jedi cuyos maestros están en el archivo;
h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.'''


#!carga
file_jedi = open(ruta_del_archivo, 'r')
read_lines = file_jedi.readlines()
file_jedi.close()

name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()

print('----------------------------------------------------------------------------')

#!a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
read_lines.pop(0)
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop() 
    name_tree.insert_node(jedi[0], index+2)
    specie_tree.insert_node(jedi[2], index+2)
    ranking_tree.insert_node(jedi[1], index+2)
    
print('Arboles por nombre, ranking y especie creados')
    
print('----------------------------------------------------------------------------')


#!b. realizar un barrido inorden del árbol por nombre y ranking;
print("Barrido arbol por Nombre:")
for elemento in name_tree:
    print(elemento)
print("\nBarrido arbol por Ranking:")
for elemento in specie_tree:
    print(elemento)
    
print('----------------------------------------------------------------------------')
    
#!c. realizar un barrido por nivel de los árboles por ranking y especie;
print("Barrido arbol por Ranking:")
ranking_tree.level_order_traversal()

print("\nBarrido arbol por Especie:")
specie_tree.level_order_traversal()

print('----------------------------------------------------------------------------')

#!d. mostrar toda la información de Yoda y Luke Skywalker;
def mostrar_informacion_personajes(nombre1, nombre2, ruta_archivo):
 with open(ruta_archivo, 'r') as file_jedi:
            for linea_jedi in file_jedi:
                jedi_info = linea_jedi.strip().split(';')  
                nombre = jedi_info[0].strip().lower()  

                if nombre == nombre1.lower() or nombre == nombre2.lower():
                    print("Información del personaje:")
                    print(f"Nombre: {jedi_info[0]}")
                    print(f"Especie: {jedi_info[2]}")
                    print(f"Año de Nacimiento: {jedi_info[6]}")
                    print(f"Color de Sable de Luz: {jedi_info[4]}")
                    print(f"Ranking: {jedi_info[1]}")
                    print(f"Maestro: {jedi_info[3]}")
                    print()  
nombre1 = "Yoda"
nombre2 = "Luke Skywalker"
mostrar_informacion_personajes(nombre1, nombre2, ruta_del_archivo)

print('----------------------------------------------------------------------------')

#!e. mostrar todos los Jedi con ranking “Jedi Master”;
def mostrar_jedi_master(ruta_archivo):
    ranking_tree = BinaryTree()
    with open(ruta_archivo, 'r') as file_jedi:
            for linea_jedi in file_jedi:
                ranking_tree.insert_node(linea_jedi, linea_jedi.split(';')[1])  
    jedi_master_info = ranking_tree.search_by_ranking("Jedi Master")
    if jedi_master_info:
        print("Jedi con ranking 'Jedi Master':")
        for info in jedi_master_info:
            print("Nombre:", info[0])
            print("Ranking:", info[1])
            print()
mostrar_jedi_master(ruta_del_archivo)

print('----------------------------------------------------------------------------')

#!f. listar todos los Jedi que utilizaron sabe de luz color verde;
def listar_jedi_con_lightsaber_verde(ruta_archivo):
    lightsaber_color_tree = BinaryTree()
    with open(ruta_archivo, 'r') as file_jedi:
            for linea_jedi in file_jedi:
                lightsaber_color_tree.insert_node(linea_jedi, linea_jedi.split(';')[4])  
    print(f"El archivo '{ruta_archivo}' no se encontró.")
    jedi_con_lightsaber_verde_info = lightsaber_color_tree.search_by_lightsaber_color("green")
    if jedi_con_lightsaber_verde_info:
        print("Jedi que utilizaron sables de luz de color verde:")
        for info in jedi_con_lightsaber_verde_info:
            print("Nombre:", info[0])
            print("Color de Sable de Luz:", info[4])
listar_jedi_con_lightsaber_verde(ruta_del_archivo)

print('----------------------------------------------------------------------------')

#!g. listar todos los Jedi cuyos maestros están en el archivo;
def listar_jedi_con_maestros_en_archivo(ruta_archivo):
    master_tree = BinaryTree()
    with open(ruta_archivo, 'r') as file_jedi:
        for linea_jedi in file_jedi:
            jedi_info = linea_jedi.strip().split(';')
            maestro = jedi_info[3].strip()  
            if maestro != '-':
                master_tree.insert_node(linea_jedi, maestro)
    jedi_con_maestros_en_archivo_info = master_tree.search_by_master_in_file(ruta_archivo)
    if jedi_con_maestros_en_archivo_info:
        print("Jedi cuyos maestros están en el archivo:")
        for info in jedi_con_maestros_en_archivo_info:
            print("Nombre:", info[0])
            print("Maestro:", info[3])
            print()
listar_jedi_con_maestros_en_archivo(ruta_del_archivo)

print('----------------------------------------------------------------------------')

#!h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
print('Jedis de especie “Togruta” o “Cerean”')
def mostrar_jedi_por_especie(ruta_archivo, especies):
    with open(ruta_archivo, 'r') as file_jedi:
        for linea_jedi in file_jedi:
            jedi_info = linea_jedi.strip().split(';')
            nombre = jedi_info[0]
            especie = jedi_info[2]
            if especie in especies:
                print("Nombre:", nombre)
                print("Especie:", especie)
                print()
especies_deseadas = ["togruta", "cerean"]
mostrar_jedi_por_especie(ruta_del_archivo, especies_deseadas)

print('----------------------------------------------------------------------------')

#!i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
print('Jedis que comienzan con la letra A y los que contienen un “-” en su nombre')
def listar_jedi_por_letra_y_caracter(ruta_archivo, letra, caracter):
    with open(ruta_archivo, 'r') as file_jedi:
        for linea_jedi in file_jedi:
            jedi_info = linea_jedi.strip().split(';')
            nombre = jedi_info[0]
            if nombre.startswith(letra) or caracter in nombre:
                print("Nombre:", nombre)
                print()
letra_deseada = "a"
caracter_deseado = "-"
listar_jedi_por_letra_y_caracter(ruta_del_archivo, letra_deseada, caracter_deseado)

print('----------------------------------------------------------------------------')





