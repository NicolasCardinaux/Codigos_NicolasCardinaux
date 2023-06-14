'''Desarrollar una función recursiva que permita contar cuantas veces
aparece una determinada palabra, en un vector de palabras.'''
def contar(vec, palabra):
    if not vec:
        return 0
    if vec[0] == palabra:
        return 1 + contar(vec[1:], palabra)
    else:
        return contar(vec[1:], palabra)
    
vec = ['mesa', 'auto', 'mesa', 'silla', 'hola', 'cpu', 'mesa', 'telefono',]
palabra = 'mesa'
resultado = contar(vec, palabra)
print('---------------------------------------------------------------')

print("La palabra '{}' aparece {} veces.".format(palabra, resultado))

print('---------------------------------------------------------------')
