
'''23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
resuelva las siguientes consultas:
a. listado inorden de las criaturas y quienes la derrotaron;
b. se debe permitir cargar una breve descripción sobre cada criatura;
c. mostrar toda la información de la criatura Talos;
d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
o dios que la capturo;
h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
Erimanto indicando que Heracles las atrapó;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;
k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles.'''
from arbolbinario import BinaryTree
criaturas = BinaryTree()

lista = [
{'Criaturas': 'Ceto',"Derrotado por": "-"},{"Criaturas": "Cerda de Cromión","Derrotado por":"Teseo"},
{'Criaturas':"Tifón" ,"Derrotado por":"Zeus"},{"Criaturas": "Ortro" ,"Derrotado por":"Heracles"},
{'Criaturas':"Equidna" ,"Derrotado por":"Argos Panoptes" },{"Criaturas":"Toro de Creta" ,"Derrotado por":"Teseo"},
{'Criaturas':"Dino" ,"Derrotado por":"-" },{"Criaturas":"Jabalí de Calidón" ,"Derrotado por":"Atalanta"},
{'Criaturas':"Pefredo" ,"Derrotado por":"-" },{"Criaturas":"Carcinos" ,"Derrotado por":"-"},
{'Criaturas':"Enio" ,"Derrotado por":"-" },{"Criaturas":"Gerión" ,"Derrotado por":"Heracles"},
{'Criaturas':"Escila" ,"Derrotado por":"-"},{"Criaturas": "Cloto" ,"Derrotado por":"-"},
{'Criaturas':"Caribdis" ,"Derrotado por":"-" },{"Criaturas":"Láquesis" ,"Derrotado por":"-"},
{'Criaturas':"Euríale","Derrotado por": "-" },{"Criaturas":"Átropos" ,"Derrotado por":"-"},
{'Criaturas':"Esteno" ,"Derrotado por":"-" },{"Criaturas":"Minotauro de Creta" ,"Derrotado por":"Teseo"},
{'Criaturas':"Medusa","Derrotado por": "Perseo" },{"Criaturas":"Harpías" ,"Derrotado por":"-"},
{'Criaturas':"Ladón" ,"Derrotado por":"Heracles",},{"Criaturas":"Argos Panoptes" ,"Derrotado por":"Hermes"},
{'Criaturas':"Águila del Cáucaso" ,"Derrotado por":"-" },{"Criaturas":"Aves del Estínfalo" ,"Derrotado por":"-"},
{'Criaturas':"Quimera" ,"Derrotado por":"Belerofonte" },{"Criaturas":"Talos" ,"Derrotado por":"Medea"},
{'Criaturas':"Hidra de Lerna" ,"Derrotado por":"Heracles" },{"Criaturas":"Sirenas" ,"Derrotado por":"-"},
{'Criaturas':"León de Nemea" ,"Derrotado por":"Heracles" },{"Criaturas":"Pitón" ,"Derrotado por":"Apolo"},
{'Criaturas':"Esfinge" ,"Derrotado por":"Edipo" },{"Criaturas":"Cierva de Cerinea" ,"Derrotado por":"-"},
{'Criaturas':"Dragón de la Cólquida" ,"Derrotado por":"-" },{"Criaturas":"Basilisco" ,"Derrotado por":"-"},
{'Criaturas':"Cerbero","Derrotado por": "-" },{"Criaturas":"Jabalí de Erimanto","Derrotado por":"-"}]

print('----------------------------------------------------------------------------')

for criatura in lista:
    criaturas.insert_node(criatura['Criaturas'], criatura['Derrotado por'])

#!a. listado inorden de las criaturas y quienes la derrotaron;
print('Inorden de las Criaturas y quienes la derrotaron')
criaturas.inordenCriaturasDerrotados()
print('----------------------------------------------------------------------------')

#! b. se debe permitir cargar una breve descripción sobre cada criatura;
print('Descripcion agregada segun corresponda:')
#Se puede agregar una descripcion para la criatura deceada segun sea necesario.
criaturas.agregarDescripcion("Tifón", "Criatura gigante de la mitología griega.")
criaturas.agregarDescripcion("Talos", "Guardián de bronce de la mitología griega.")
criaturas.agregarDescripcion("Cerbero", "Feroz perro guardián del inframundo.")
criaturas.agregarDescripcion("Toro de Creta", "Impetuoso toro de Creta que asolaba la isla.")
criaturas.agregarDescripcion("Cierva Cerinea", "Rápida cierva dorada de Cerinea.")
criaturas.agregarDescripcion("Jabalí de Erimanto", "Feroz jabalí que causaba estragos en Erimanto.")
for criatura_nombre in ["Tifón", "Talos"]:
    criatura = criaturas.search(criatura_nombre)
    if criatura:
        descripcion = criatura.tercer_values if criatura.tercer_values is not None else "Descripción no disponible"
        print(f"{criatura.value}: {descripcion}")
        
print('----------------------------------------------------------------------------')


#! c. mostrar toda la información de la criatura Talos;
print('Informacion de Talos:')
criaturas.mostrar_info_criatura("Talos")

print('----------------------------------------------------------------------------')

##! d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de Criaturas;
top_heroes = criaturas.heroes_que_derrotaron_mas_criaturas(lista)
print("Los 3 héroes o dioses que derrotaron mayor cantidad de criaturas son:")
for heroe, cantidad in top_heroes:
    print(f"{heroe}: {cantidad} criaturas derrotadas")

print('----------------------------------------------------------------------------')
    
#!e. listar las criaturas derrotadas por Heracles;
print("Criaturas derrotadas por Heracles:")
criaturas.criaturasDerrotoHeracles()

print('----------------------------------------------------------------------------')

#!f. listar las criaturas que no han sido derrotadas;
print("Crituras no derrotadas:")
criaturas.criaturasNoDerrotadas()

print('----------------------------------------------------------------------------')

#!g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
print('El campo fue agregado')

print('----------------------------------------------------------------------------')


#! h. modifique los nodos de las Criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
print('Modificacion, capturados por Heracles')
def modificarCaptura(criaturas, criatura_nombre, capturador):
    criatura = criaturas.search(criatura_nombre)
    if criatura:
        criatura.cuarto_values = capturador 
modificarCaptura(criaturas, "Cerbero", "Heracles")
criaturas.mostrar_capturador("Cerbero")
modificarCaptura(criaturas, "Toro de Creta", "Heracles")
criaturas.mostrar_capturador("Toro de Creta")
modificarCaptura(criaturas, "Cierva de Cerinea", "Heracles")
criaturas.mostrar_capturador("Cierva de Cerinea")
modificarCaptura(criaturas, "Jabalí de Erimanto", "Heracles")
criaturas.mostrar_capturador("Jabalí de Erimanto")

print('----------------------------------------------------------------------------')

#!i. se debe permitir búsquedas por coincidencia;
print('Busqueda por coincidencia:')
coincidencias = criaturas.buscarPorCoincidencia("Cer")
print('Buscado: Cer')
for criatura in coincidencias:
    print(f'Criatura: {criatura.value} Derrotado por: {criatura.other_values}')

print('----------------------------------------------------------------------------')

#!j. eliminar al Basilisco y a las Sirenas
criaturas.delete_node('Basilisco')
criaturas.delete_node('Sirenas')
print('Eliminado exitosamente')

print('----------------------------------------------------------------------------')

#!k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
value = criaturas.search("Aves del Estínfalo")
if value:
    if value.cuarto_values:
        value.cuarto_values += " y Heracles"
    else:
        value.cuarto_values = "Heracles"
    print('Nodo Modificado')
else:
    print("La criatura 'Aves del Estínfalo' no se encuentra en la lista.")
criaturas.mostrar_info_criatura("Aves del Estínfalo")

print('----------------------------------------------------------------------------')


#!l. modifique el nombre de la criatura Ladón por Dragón Ladón;
valu = criaturas.search("Ladón")
if valu:
    valu.value = "Dragón Ladón"
else:
    print("La criatura 'Ladón' no se encuentra en la lista.")
print('La criatura Ladón fue modificada exitosamente por Dragón Ladón.')

print('----------------------------------------------------------------------------')

#!m. realizar un listado por nivel del árbol;
print("Listado por nivel del árbol:")
criaturas.listadoPorNivel()

print('----------------------------------------------------------------------------')

#!n. muestre las criaturas capturadas por Heracles.
print("Criaturas atrapadas por Heracles:")
criaturas.search_capturados_Heracles()

print('----------------------------------------------------------------------------')




