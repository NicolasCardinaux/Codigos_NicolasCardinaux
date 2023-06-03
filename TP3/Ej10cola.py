'''Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
resolver las siguientes actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
la palabra "Python", si perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
11:43 y las 15:57, y determinar cuántas son.'''
class Cola:
    def __init__(self):
        self.__elementos = []

    def arrive(self, value):
        self.__elementos.append(value)

    def atencion(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):
        return len(self.__elementos)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atencion()
            self.arrive(aux)
            return aux
        
    def __repr__(self):
        return f"Cola: {self.__elementos}"
        
    


class Noti:
    def __init__(self, hora, app, mensaje):
        self.hora = hora
        self.app = app
        self.mensaje = mensaje

    def __repr__(self):
        return f"Hora: {self.hora}, App: {self.app}, Mensaje: {self.mensaje}\n"

cola_notificaciones = Cola()
cola_notificaciones.arrive(Noti(9.23, "Facebook", "Juan quiere ser tu amigo"))
cola_notificaciones.arrive(Noti(10.15, "Twitter", "Python vs Java"))
cola_notificaciones.arrive(Noti(11.02, "Instagram", "Te han etiquetado en una foto"))
cola_notificaciones.arrive(Noti(12.45, "WhatsApp", "Mensaje de texto: Hola, ¿ya está listo el tp de Python?"))
cola_notificaciones.arrive(Noti(13.30, "Snapchat", "Has recibido un nuevo snap"))
cola_notificaciones.arrive(Noti(14.18, "LinkedIn", "Nueva oferta de empleo con relación a Python"))
cola_notificaciones.arrive(Noti(15.05, "Pinterest", "Nuevo pin en tu tablero"))
cola_notificaciones.arrive(Noti(16.20, "Facebook", "Nuevo mensaje en el grupo"))
cola_notificaciones.arrive(Noti(17.13, "Twitter", "Sabes programar en Python"))
cola_notificaciones.arrive(Noti(18.40, "TikTok", "Tu video se ha vuelto viral"))

print('----------------------------------------------------------------------------')

#! a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
def eliminar_notificaciones_facebook(cola):
    tamaño = cola.size()
    for _ in range(tamaño):
        notificacion = cola.atencion()
        if notificacion.app != "Facebook":
            cola.arrive(notificacion)

eliminar_notificaciones_facebook(cola_notificaciones)
print("Notificaciones de Facebook eliminadas")
print("Cola de notificaciones actualizada:", cola_notificaciones)

print('----------------------------------------------------------------------------')

#! b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluyala palabra "Python", si perder datos en la cola;
def mostrar_notificaciones_twitter_python(cola):
    tamaño = cola.size()
    notificaciones = []
    for _ in range(tamaño):
        notificacion = cola.atencion()
        if notificacion.app == "Twitter" and "Python" in notificacion.mensaje:
            notificaciones.append(notificacion)
        cola.arrive(notificacion)
    return notificaciones

notificaciones_twitter_python = mostrar_notificaciones_twitter_python(cola_notificaciones)
print("Notificaciones de Twitter que contienen 'Python':")
for notificacion in notificaciones_twitter_python:
    print(notificacion)

print('----------------------------------------------------------------------------')

#! c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
def contar_notificaciones_temporales(cola):
    pila_temporal = []
    contador = 0
    tamaño = cola.size()
    for _ in range(tamaño):
        notificacion = cola.atencion()
        if 11.43 <= notificacion.hora <= 15.57:
            pila_temporal.append(notificacion)
            contador += 1
        else:
            cola.arrive(notificacion)
    while len(pila_temporal) > 0:
        cola.arrive(pila_temporal.pop())
    return contador

cantidad_notificaciones_temporales = contar_notificaciones_temporales(cola_notificaciones)
print("Cantidad de notificaciones temporales:", cantidad_notificaciones_temporales)

print('----------------------------------------------------------------------------')