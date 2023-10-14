'''5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
se (MCU), desarrollar un algoritmo que contemple lo siguiente:

a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
leano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:
I. determinar cuántos nodos tiene cada árbol;
II. realizar un barrido ordenado alfabéticamente de cada árbol.'''
from arbolbinario import BinaryTree


lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': False},
    {'name': 'deadpool', 'heroe': True},
]


arbol = BinaryTree()
for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])
    
print('----------------------------------------------------------------------------')

#!B. listar los villanos ordenados alfabéticamente;
print("Villanos en orden alfabético:")
arbol.listar_villanos_alfabeticamente()

print('----------------------------------------------------------------------------')

#!C. mostrar todos los superhéroes que empiezan con C
print("Superhéroes que empiezan con 'C':")
arbol.mostrar_superheroes_que_empiezan_con_C()

print('----------------------------------------------------------------------------')

#!D. determinar cuántos superhéroes hay el árbol;
cantidad_heroes = arbol.contar_heroes()  
print(f"Total de superhéroes en el árbol: {cantidad_heroes}")

print('----------------------------------------------------------------------------')

#!E. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
resultado = arbol.search_by_proximity("doctor strange")
if resultado:
    print("Resultado encontrado:", resultado.value)
target_value = "dotor strage"
new_value = "doctor strange"
arbol.search_and_modify(arbol.root, target_value, new_value)
print('Nombre Modificado')

print('----------------------------------------------------------------------------')

#!F. listar los superhéroes ordenados de manera descendente;
print("Lista de superheroes en orden decendiente:")
arbol.listar_superheroes_descendente()

print('----------------------------------------------------------------------------')


#! g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
#! Dividir el árbol en dos árboles separados: uno para héroes y otro para villanos
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

#! Mover los nodos a los árboles correspondientes
for heroe in lista_heroes:
    if heroe['heroe']:
        arbol_heroes.insert_node(heroe['name'], True)
    else:
        arbol_villanos.insert_node(heroe['name'], False)

#! I. determinar cuántos nodos tiene cada árbol;
nodos_heroes = arbol_heroes.contar_nodos()
nodos_villanos = arbol_villanos.contar_nodos()

print(f'Árbol de Héroes tiene {nodos_heroes} nodos.')
print(f'Árbol de Villanos tiene {nodos_villanos} nodos.')

#! II. realizar un barrido ordenado alfabéticamente de cada árbol.
print('Barrido alfabético del Árbol de Héroes:')
arbol_heroes.inorden()

print('Barrido alfabético del Árbol de Villanos:')
arbol_villanos.inorden()

print('----------------------------------------------------------------------------')




