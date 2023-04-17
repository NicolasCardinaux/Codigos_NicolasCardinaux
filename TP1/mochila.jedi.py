#Ejercicio Nº 22
'''El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;

b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
car para encontrarlo;

c. Utilizar un vector para representar la mochila.'''

def usar_la_fuerza(mochila, index=0, objetos_sacados=[], sable_encontrado=False):
    if index >= len(mochila):
        return (objetos_sacados, False)
    elif mochila[index] == "sable de luz":
        objetos_sacados.append(mochila[index])
        sable_encontrado = True
        return (objetos_sacados, sable_encontrado)
    else:
        objetos_sacados.append(mochila[index])
        return usar_la_fuerza(mochila, index + 1, objetos_sacados, sable_encontrado)

mochila = ["comida", "agua", "medicamento", "sable de luz", "ropa"]
objetos_sacados, sable_encontrado = usar_la_fuerza(mochila)
if sable_encontrado:
    print(f"Se sacaron {len(objetos_sacados)-1} objetos antes de encontrar el sable de luz.")
    print("Los objetos sacados son:", objetos_sacados)
else:
    print("No se encontró un sable de luz en la mochila.")


