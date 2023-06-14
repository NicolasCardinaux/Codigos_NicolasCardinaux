'''Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
cual se almacenaban en una pila en cada misión de caza que
emprendió (con la siguiente información planeta visitado, a quien
capturado, costo de la recompensa), resolver las siguientes
actividades:
a. Mostrar los planetas visitados en el orden hizo las misiones.
b. Determinar cuántos créditos galácticos recaudo en total.
c. Determinar el número de la misión en que capturo a Han Solo
y en que planeta fue, suponga que dicha misión está cargada.'''

class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.__elements == stack_aux.__elements
        else:
            return False

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato

    def size(self):
        return len(self.__elements)

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]


class Bitacora:
    def __init__(self, mision, planeta, capturado, costo):
        self.mision = mision
        self.planeta = planeta
        self.capturado = capturado
        self.costo = costo

    def __repr__(self):
        return f"Mision: {self.mision}, Planeta: {self.planeta}, Capturado: {self.capturado}, Costo: {self.costo}"


pila_bitacoras = Pila()
pila_bitacoras.push(Bitacora(7, "jupiter", "destructor", 5000))
pila_bitacoras.push(Bitacora(13, "Marte", "Pirata", 2000))
pila_bitacoras.push(Bitacora(2, "Venus", "Contrabandista", 3000))
pila_bitacoras.push(Bitacora(12, "Tierra", "Asesino", 10000))
pila_bitacoras.push(Bitacora(11, "Saturno", "Ladrón", 1500))
pila_bitacoras.push(Bitacora(12, "Urano", "Terrorista", 4000))
pila_bitacoras.push(Bitacora(15, "Neptuno", "Espía", 2500))
pila_bitacoras.push(Bitacora(14, "Plutón", "Gánster", 3500))
pila_bitacoras.push(Bitacora(7, "Mercurio", "Rebelde", 1800))
pila_bitacoras.push(Bitacora(3, "Luna", "Saboteador", 2200))
pila_bitacoras.push(Bitacora(1, "Marte", "Pirata", 2400))
pila_bitacoras.push(Bitacora(10, "Jupiter", "Contrabandista", 3500))
pila_bitacoras.push(Bitacora(9, "Tierra", "Asesino", 1000))
pila_bitacoras.push(Bitacora(6, "Saturno", "Han Solo", 25000))
pila_bitacoras.push(Bitacora(8, "Urano", "Terrorista", 4000))

print('--------------------------------------------------------')

#!a. Mostrar los planetas visitados en el orden hizo las misiones.
print('Planetas visitados:')
bitacoras_lista = []
while pila_bitacoras.size() > 0:
    bitacoras_lista.append(pila_bitacoras.pop())
bitacoras_ordenadas = sorted(bitacoras_lista, key=lambda b: b.mision)
for bitacora in bitacoras_ordenadas:
    print(f"Misión {bitacora.mision}: Planeta: {bitacora.planeta}")

print('--------------------------------------------------------')

#! b. Determinar cuántos créditos galácticos recaudo en total.
total_creditos = 0
for bitacora in bitacoras_lista:
    total_creditos += bitacora.costo
print("Total de créditos galácticos recaudados:", total_creditos)

print('--------------------------------------------------------')

#! c. Determinar el número de la misión en que capturo a Han Solo  y en que planeta fue, suponga que dicha misión está cargada.
for bitacora in bitacoras_lista:
    if bitacora.capturado == "Han Solo":
        numero_mision_han_solo = bitacora.mision
        planeta_han_solo = bitacora.planeta
        break  
if numero_mision_han_solo is not None and planeta_han_solo is not None:
    print("Han Solo fue capturado en la misión número:", numero_mision_han_solo)
    print("Planeta en el que fue capturado:", planeta_han_solo)
    
print('--------------------------------------------------------')
