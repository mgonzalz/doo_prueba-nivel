from subclases.bicicleta import Bicicleta
from subsubclases.motocicleta import Motocicleta
from subsubclases.camioneta import Camioneta
from subclases.coche import Coche

def catalogar(lista):
    '''
        Modifica la función catalogar() para que reciba un argumento
        optativo ruedas, haciendo que muestre únicamente los que su
        número de ruedas concuerde con el valor del argumento. También
        debe mostrar un mensaje "Se han encontrado {} vehículos con {}
        ruedas:" únicamente si se envía el argumento ruedas. Ponla a
        prueba con 0, 2 y 4 ruedas como valor.
        Recordatorio
        Puedes utilizar el atributo especial de clase name para recuperar el nombre de
        la clase de un objeto:
    '''
    for i in lista:
        print(type(i).__name__, ": ",i)


if __name__ == "__main__":
    vehiculos = []

    coche = Coche("azul", 150, 4, 1200)
    vehiculos.append(coche)


    b = Bicicleta("rojo", 2, "deportiva")
    vehiculos.append(b)

    m = Motocicleta("rojo", 3, "deportiva", 180, 900)
    vehiculos.append(m)

    c = Camioneta("azul", 4, 150, 1200, 70)
    vehiculos.append(c)

    catalogar(vehiculos)
