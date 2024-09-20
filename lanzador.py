from subclases.bicicleta import Bicicleta
from subsubclases.motocicleta import Motocicleta
from subsubclases.camioneta import Camioneta
from subclases.coche import Coche


def catalogar(lista, ruedas=None):
    '''
        Modifica la función catalogar() para que reciba un argumento
        optativo ruedas, haciendo que muestre únicamente los que su
        número de ruedas concuerde con el valor del argumento. También
        debe mostrar un mensaje "Se han encontrado {} vehículos con {}
        ruedas:" únicamente si se envía el argumento ruedas. Ponla a
        prueba con 0, 2 y 4 ruedas como valor.
    '''
    contador = 0
    for i in lista:
        if i.get_ruedas() == ruedas or ruedas is None:
            print(type(i).__name__, ": ",i)
            contador += 1
    
    print("Se han encontrado {} vehículos con {} ruedas".format(contador, ruedas))


def main():
    vehiculos = []

    coche = Coche("azul", 4, 150, 1200) # color, ruedas, velocidad, cilindrada
    vehiculos.append(coche)


    b = Bicicleta("rojo", 2, "deportiva") # color, ruedas, tipo
    vehiculos.append(b)

    m = Motocicleta("rojo", 3, "deportiva", 180, 900) # color, ruedas, tipo, velocidad, cilindrada
    vehiculos.append(m)

    c = Camioneta("azul", 4, 150, 1200, 70) # color, ruedas, velocidad, cilindrada, carga
    vehiculos.append(c)

    catalogar(vehiculos, 4)
    catalogar(vehiculos, 2)
    catalogar(vehiculos)
