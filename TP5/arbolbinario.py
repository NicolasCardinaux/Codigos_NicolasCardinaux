import linecache
from collections import deque
class Cola():

    def __init__(self):
        self.__elementos = []

    def arrive(self, value):
        self.__elementos.append(value)

    def atention(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):
        return len(self.__elementos)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux



def get_value_from_file(file_name, index):
    line = linecache.getline(file_name, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split


class NodeTree():
    def __init__(self, value, other_values=None, tercer_values=None, cuarto_values=None, descripcion=None, capturador=None):
        self.value = value
        self.other_values = other_values
        self.tercer_values = tercer_values
        self.cuarto_values = cuarto_values
        self.descripcion = descripcion  
        self.capturador = capturador
        self.left = None
        self.right = None
        self.height = 0


   
class BinaryTree:

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root
    


    def insert_node(self, value, derrotado_por):
        def __insertar(root, value, derrotado_por):
            if root is None:
                return NodeTree(value, derrotado_por)
            elif value < root.value:
                root.left = __insertar(root.left, value, derrotado_por)
            else:
                root.right = __insertar(root.right, value, derrotado_por)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, derrotado_por)

            
    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(node.value)
                # a = input()
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    def inorden_file(self, file_name):
        def __inorden_file(root, file_name):
            if root is not None:
                __inorden_file(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                print(root.value, value[0])
                __inorden_file(root.right, file_name)

        __inorden_file(self.root, file_name)

    def inorden_file_lightsaber(self, file_name, lightsaber_color):
        def __inorden_file_lightsaber(root, file_name, lightsaber_color):
            if root is not None:
                __inorden_file_lightsaber(root.left, file_name, lightsaber_color)
                value = get_value_from_file(file_name, root.other_values)
                if lightsaber_color in value[4].split('/'):
                    print(root.value, value[4].split('/'))
                __inorden_file_lightsaber(root.right, file_name, lightsaber_color)

        __inorden_file_lightsaber(self.root, file_name, lightsaber_color)

    def inorden_super_or_villano(self, is_hero):
        def __inorden_s_v(root, is_hero):
            if root is not None:
                __inorden_s_v(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden_s_v(root.right, is_hero)

        __inorden_s_v(self.root, is_hero)

    def inorden_start_with(self, cadena):
        def __inorden_start_with(root, cadena):
            if root is not None:
                __inorden_start_with(root.left, cadena)
                if root.other_values is True and root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with(root.right, cadena)

    def inorden_start_with_jedi(self, cadena):
        def __inorden_start_with_jedi(root, cadena):
            if root is not None:
                __inorden_start_with_jedi(root.left, cadena)
                if root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with_jedi(root.right, cadena)

        __inorden_start_with_jedi(self.root, cadena)
        

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value, root.height)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)
        
    def search_by_lightsaber_color(self, lightsaber_color):
        def __search_by_lightsaber_color(root, lightsaber_color):
            results = []
            if root is not None:
                jedi_info = root.value.strip().split(';')  
                lightsaber_colors = jedi_info[4].strip().lower().split('/')  
                if 'green' in lightsaber_colors:
                    results.append(jedi_info)
                results.extend(__search_by_lightsaber_color(root.left, lightsaber_color))
                results.extend(__search_by_lightsaber_color(root.right, lightsaber_color))
            return results
        return __search_by_lightsaber_color(self.root, lightsaber_color)
    
    def search_by_master_in_file(self, file_path):
        def __search_by_master_in_file(root, file_path):
            results = []
            if root is not None:
                jedi_info = root.value.strip().split(';') 
                maestro = jedi_info[3].strip()  
                with open(file_path, 'r') as file:
                    if maestro in file.read():
                        results.append(jedi_info)
                results.extend(__search_by_master_in_file(root.left, file_path))
                results.extend(__search_by_master_in_file(root.right, file_path))
            return results
        return __search_by_master_in_file(self.root, file_path)
    
    def search_by_ranking(self, ranking):
        def __search_by_ranking(root, ranking):
            results = []
            if root is not None:
                jedi_info = root.value.strip().split(';') 
                jedi_ranking = jedi_info[1].strip().lower()  
                if jedi_ranking == ranking.lower():
                    results.append(jedi_info)
                results.extend(__search_by_ranking(root.left, ranking))
                results.extend(__search_by_ranking(root.right, ranking))
            return results
        return __search_by_ranking(self.root, ranking)
        



    def search_by_coincidence(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)
    
    def listar_villanos_alfabeticamente(self):
        def __listar_villanos_alfabeticamente(root):
            if root is not None:
                __listar_villanos_alfabeticamente(root.left)
                if not root.other_values: 
                    print(root.value)
                __listar_villanos_alfabeticamente(root.right)

        __listar_villanos_alfabeticamente(self.root)
        
    def mostrar_superheroes_que_empiezan_con_C(self):
        def __mostrar_superheroes_que_empiezan_con_C(root):
            if root is not None:
                __mostrar_superheroes_que_empiezan_con_C(root.left)
                if root.other_values and root.value.startswith('c'):
                    print(root.value)
                __mostrar_superheroes_que_empiezan_con_C(root.right)
        __mostrar_superheroes_que_empiezan_con_C(self.root)
        
    def levenshtein_distance(self, s1, s2):
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)
        if len(s2) == 0:
            return len(s1)
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]
    
    def level_order_traversal(self):
        if self.root is None:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            print(node.value, node.other_values)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                

    
    def contar_nodos(self):
        def contar_recursivo(root):
            if root is None:
                return 0
            return 1 + contar_recursivo(root.left) + contar_recursivo(root.right)

        return contar_recursivo(self.root)

        return contar_recursivo(self.root)
    def search_by_proximity(self, target_value):
        def __search_by_proximity(root, target_value):
            if root is None:
                return None
            distance = self.levenshtein_distance(root.value.lower(), target_value.lower())
            max_distance = 3  #
            if distance <= max_distance:
                return root
            if target_value < root.value:
                return __search_by_proximity(root.left, target_value)
            else:
                return __search_by_proximity(root.right, target_value)
        return __search_by_proximity(self.root, target_value)
    
    def search_and_modify(self, current_node, target_value, new_value):
        if current_node is None:
            return
        if current_node.value == target_value:
            current_node.value = new_value
        self.search_and_modify(current_node.left, target_value, new_value)
        self.search_and_modify(current_node.right, target_value, new_value)
    
   
    def inorden_superheroes(self, heroes_list):
        def __inorden_superheroes(root):
            if root is not None:
                __inorden_superheroes(root.left)
                if root.other_values is True:  
                    heroes_list.append(root.value)
                __inorden_superheroes(root.right)

        __inorden_superheroes(self.root)

    def listar_superheroes_descendente(self):
        heroes_list = []
        self.inorden_superheroes(heroes_list)
        heroes_list.sort(reverse=True)  
        for hero in heroes_list:
            print(hero)




    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value

            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value

    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count

        return __contar(self.root, value)
    
    
    def contar_heroes(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is True:
                    count = 1
                count += __contar_heroes(root.left)
                count += __contar_heroes(root.right)
            return count

        return __contar_heroes(self.root)
    
    def __iter__(self):
        return self.inorder_generator()

    def inorder_generator(self):
        def __inorder_generator(node):
            if node:
                yield from __inorder_generator(node.left)
                yield node.value
                yield from __inorder_generator(node.right)

        return __inorder_generator(self.root)
    
    #!Ejercicio 23
    
    def inordenCriaturasDerrotados(self):
        def __inordenCriaturasDerrotados(root):
            if root is not None:
                __inordenCriaturasDerrotados(root.left)
                print(f'Criatura: {root.value} Derrotado por: {root.other_values}')
                __inordenCriaturasDerrotados(root.right)

        __inordenCriaturasDerrotados(self.root)
        
    def agregarDescripcion(self, criatura_nombre, descripcion):
     def __buscar_y_agregar_descripcion(root, quien, mensaje):
        if root is not None:
            if root.value == quien:
                root.tercer_values = mensaje  
            __buscar_y_agregar_descripcion(root.left, quien, mensaje)
            __buscar_y_agregar_descripcion(root.right, quien, mensaje)

     __buscar_y_agregar_descripcion(self.root, criatura_nombre, descripcion)

   
    def mostrar_info_criatura(self, criatura_nombre):
     criatura = self.search(criatura_nombre)
     if criatura:
        descripcion = criatura.tercer_values if criatura.tercer_values is not None else "Descripción no disponible"
        capturador = criatura.cuarto_values if criatura.cuarto_values is not None else "Capturador desconocido"
        print(f'Criatura: {criatura.value} Derrotado por: {criatura.other_values} Descripción: {descripcion} Capturado Por: {capturador}')
     else:
        print(f"La criatura '{criatura_nombre}' no se encuentra en la lista.")
        
    def mostrar_capturador(self, criatura_nombre):
     criatura = self.search(criatura_nombre)
     if criatura:
        capturador = criatura.cuarto_values if criatura.cuarto_values is not None else "Capturador desconocido"
        print(f"Criatura: {criatura.value} Capturador: {capturador}")
     else:
        print(f"La criatura '{criatura_nombre}' no se encuentra en la lista.")
        
    def heroes_que_derrotaron_mas_criaturas(cls, criaturas):
        heroes = {}
        for criatura in criaturas:
            derrotado_por = criatura["Derrotado por"]
            if derrotado_por != "-":
                if derrotado_por in heroes:
                    heroes[derrotado_por] += 1
                else:
                    heroes[derrotado_por] = 1

        heroes_ordenados = sorted(heroes.items(), key=lambda x: x[1], reverse=True)
        top_heroes = heroes_ordenados[:3]
        return top_heroes
        
    def criaturasDerrotoHeracles(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                if (root.other_values == "Heracles"):
                    print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    def criaturasNoDerrotadas(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                if (root.other_values == "-"):
                    print(root.value)
                __inorden(root.right)

        __inorden(self.root)
        
    def buscarPorCoincidencia(self, termino):
        coincidencias = []
        def buscar_coincidencia(root, termino):
            if root is not None:
                if termino in root.value:
                    coincidencias.append(root)
                buscar_coincidencia(root.left, termino)
                buscar_coincidencia(root.right, termino)
        buscar_coincidencia(self.root, termino)
        return coincidencias
    
    def mostrar_info_criaturaa(self, criatura_nombre):
     criatura = self.search(criatura_nombre)
     if criatura:
        descripcion = criatura.tercer_values if criatura.tercer_values is not None else "Descripción no disponible"
        print(f'Criatura: {criatura.value} Derrotado por: {criatura.other_values} Descripción: {descripcion}')
     else:
        print(f"La criatura '{criatura_nombre}' no se encuentra en la lista.")

    def listadoPorNivel(self):
        if self.root is None:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    def search_capturados_Heracles(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                if root.cuarto_values == "Heracles":
                    print(root.value)
                __inorden(root.right)

        __inorden(self.root)

