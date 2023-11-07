
import linecache
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

    def __init__(self, value, other_values=None, tercer_values=None, cuarto_values=None):
        self.value = value
        self.other_values = other_values
        self.tercer_values = tercer_values
        self.cuarto_values = cuarto_values
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

    def insert_node(self, value, other_values=None , tercer_values=None, cuarto_values=None):

        def __insertar(root, value, other_values, tercer_values, cuarto_values):
            if root is None:
                return NodeTree(value, other_values, tercer_values, cuarto_values=None)
            elif value < root.value:
                root.left = __insertar(root.left, value, other_values, tercer_values, cuarto_values)
            else:
                root.right = __insertar(root.right, value, other_values, tercer_values,cuarto_values)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values, tercer_values, cuarto_values)

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
    

# ! ejercico 5
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

    def alfabetoOrden(self):
        def __alfabetoOrden(root):
            if root is not None:
                __alfabetoOrden(root.left)
                hola = root.value
                cosa = hola[0]
                if  cosa == 'c':
                    print(root.value)
                __alfabetoOrden(root.right)

        __alfabetoOrden(self.root)

    def soloVillano(self):
        def __soloVillano(root):
            if root is not None:
                __soloVillano(root.left)
                
                if  root.other_values == False:
                    print(root.value)
                
                __soloVillano(root.right)

        __soloVillano(self.root)

    def divide_tree_h_v(self, tree_hero, tree_villain):
        #used inorden villain/hero to make this one
        def divide_tree_h_v(root,tree_hero,tree_villain):
            if root is not None:
                divide_tree_h_v(root.left,tree_hero, tree_villain)
                if root.other_values is True:
                    tree_hero.insert_node(root.value,root.other_values)
                if root.other_values is False:
                    tree_villain.insert_node(root.value,root.other_values)
                divide_tree_h_v(root.right,tree_hero,tree_villain)

        divide_tree_h_v(self.root,tree_hero,tree_villain)


# !Ejercicio 6 
    def mostrarJedisMaster(self, fire):
        def __mostrarJedisMaster(root):
            if root is not None:
                __mostrarJedisMaster(root.left)

                if  root.value == 'jedi master':
                    print(get_value_from_file(fire, root.other_values)[0])

                    print(get_value_from_file(fire, root.other_values))
                    
                __mostrarJedisMaster(root.right)

        __mostrarJedisMaster(self.root)

    def listarLightGreen(self, fire):
        def __listarLightGreen(root):
            if root is not None:
                __listarLightGreen(root.left)

                if  'green' in get_value_from_file(fire, root.other_values)[4].lower()  :
                    print(get_value_from_file(fire, root.other_values)[0])

                    
                __listarLightGreen(root.right)

        __listarLightGreen(self.root)



    def agregoMaestros(self, fire):
        
        def __agregoMaestros(root):
            if root is not None:
                __agregoMaestros(root.left)

                if get_value_from_file(fire, root.other_values)[3] != '-':
                    get_value_from_file(fire, root.other_values)
                    print(get_value_from_file(fire, root.other_values))
                __agregoMaestros(root.right)

        __agregoMaestros(self.root)
    
    def especieTogrutaCerean(self, fire):
        def __especieTogrutaCerean(root):
            if root is not None:
                __especieTogrutaCerean(root.left)

                if  'cerean' in get_value_from_file(fire, root.other_values)[2].lower() or 'togruta' in get_value_from_file(fire, root.other_values)[2].lower():
                    print(get_value_from_file(fire, root.other_values)[0])

                    
                __especieTogrutaCerean(root.right)

        __especieTogrutaCerean(self.root)

    def conAoConGuion(self, fire):
        def __conAoConGuion(root):
            if root is not None:
                __conAoConGuion(root.left)
                
                hola = get_value_from_file(fire, root.other_values)[0].lower()
                cosa = hola[0]
                


                if  'a' == cosa or '-' in get_value_from_file(fire, root.other_values)[0].lower():
                    print(get_value_from_file(fire, root.other_values)[0])

                    
                __conAoConGuion(root.right)

        __conAoConGuion(self.root)


#!  ejercicio 23

    def inordenCriaturasDerrotados(self):
        def __inordenCriaturasDerrotados(root):
            if root is not None:
                __inordenCriaturasDerrotados(root.left)
                print(f'Criatura: {root.value} Derrotado por: {root.other_values} descripcion: {root.tercer_values} Capturado Por: {root.cuarto_values}')
                __inordenCriaturasDerrotados(root.right)

        __inordenCriaturasDerrotados(self.root)

    
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

    def search_by_quien(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(f'Criatura: {root.value} Derrotado por: {root.other_values} descripcion: {root.tercer_values} Capturado Por: {root.cuarto_values}')
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value)

    def search_capturados_Heracles(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                if root.cuarto_values == "Heracles":
                    print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    def inorden_ranking(self, ranking):
        def __inorden_ranking(root, ranking):
            if root is not None:
                __inorden_ranking(root.left, ranking)
                if root.other_values is not None:
                    if root.other_values not in ranking:
                        ranking[root.other_values] = 1
                    else:
                        ranking[root.other_values] += 1
                __inorden_ranking(root.right, ranking)

        __inorden_ranking(self.root, ranking)



    #! metodos del parcial

    def search_by_coincidence_with_proximi(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value) or root.value in value:
                    print(f'Pokemon: {root.value} Datos:{root.other_values}')
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value)


    def search_Number_Pokemons(self, key):
        def search(root, key):
            if root is not None:
                if root.value == key:
                    print(f"Numero de Pokemon: {root.value}. Nombre: {root.other_values[0]}. Tipo: {root.other_values[1]}")
                elif key < root.value:
                    return search(root.left, key)
                else:
                    return search(root.right, key)
        search(self.root, key)


    def inorden_Tipos(self):
        def __inorden_Tipos(root):
            if root is not None:
                __inorden_Tipos(root.left)
                if ("Agua" in root.value) or ("Eléctrico" in root.value) or ("Fuego" in root.value) or ("Planta" in root.value):
                    print(f'Pokemon: {root.other_values}')
                __inorden_Tipos(root.right)

        __inorden_Tipos(self.root)

    def inordenName(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(f"Nombre: {root.value}. Numero: {root.other_values[0]}. Tipo: {root.other_values[1]}")
                __inorden(root.right)

        __inorden(self.root)

    def inordenNumero(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(f"Numero: {root.value}. Nombre: {root.other_values[0]}. Tipo: {root.other_values[1]}")
                __inorden(root.right)

        __inorden(self.root)

    def by_level_name(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(f"Nombre: {node.value}. Numero: {node.other_values[0]}. Tipo: {node.other_values[1]}")
                # a = input()
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def contarElectricos(self):
        def __contar(root):
            count = 0
            if root is not None:
                if "Eléctrico" in root.value:
                    count = 1
                count += __contar(root.left)
                count += __contar(root.right)
            return count

        return __contar(self.root)
    
    def contarAcero(self):
        def __contar(root):
            count = 0
            if root is not None:
                if "Acero" in root.value:
                    count = 1
                count += __contar(root.left)
                count += __contar(root.right)
            return count

        return __contar(self.root)