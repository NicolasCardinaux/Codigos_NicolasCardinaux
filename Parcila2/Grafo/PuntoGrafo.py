'''2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar 
los algoritmos necesarios para resolver las siguientes tareas: 
a) cada vértice debe almacenar el nombre de un personaje, las aristas representan lacantidad 
de episodios en los que aparecieron juntos ambos personajes que se relacionan; 
b) hallar el árbol de expansión minino y determinar si contiene a Yoda; 
c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 
d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader,
Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
'''
from grafo import Grafo
from random import randint
graph = Grafo(dirigido=False)

#!d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
starwarschar = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C 3PO", "Princess Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2 D2", "BB 8"]

for i in starwarschar:
    graph.insert_vertice(i)

#!a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan; 
print('Punto a')
j=0


for i in starwarschar:
    position = graph.search_vertice(i)
    point = graph.get_element_by_index(position)
    if point[1].size() < 4:
        k = 0
        while j == 0:
            if k >= len(starwarschar):
                j=1
            else:
                place = starwarschar[k]
                positionb = graph.search_vertice(place)
                pointb = graph.get_element_by_index(positionb)
                checker = graph.is_adyacent(point[0],pointb[0])
                graph.mark_as_not_visited()
                if pointb[1].size() < 3 and point[0] != pointb[0] and checker == False:
                    value = randint(1, 20)
                    graph.insert_arist(point[0], pointb[0], value)
                    if point[1].size() == 3:
                        j=1
                k += 1
        j=0

graph.barrido()

tree_min = graph.kruskal()

i=0

#!b) hallar el árbol de expansión minino y determinar si contiene a Yoda; 
#!c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 
print('Puntos b y c')

max_value = 0
max_node = list
for tree in tree_min:
    print("Arbol Minimo")
    for node in tree.split(";"):
        value = node.split("-")
        print(node)
        if value[0]=="Yoda" or value[1]=="Yoda":
            i = 1
        if int(value[2])>max_value:
            max_node = value
    if i ==1:
        print("Yoda existe en el arbol minimo")
        print(f"Esta es la arista de valor maximo {value[0]} y {value[1]} comparten {value[2]} episodios")
