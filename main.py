from subclases.bicicleta import Bicicleta
from subsubclases.motocicleta import Motocicleta
from subsubclases.camioneta import Camioneta
from subclases.coche import Coche

if __name__ == "__main__":

    coche = Coche("azul", 150, 4, 1200)
    print(coche)
    
    b = Bicicleta("rojo", 2, "deportiva")
    print(b)

    m = Motocicleta("rojo", 3, "deportiva", 180, 900)
    print(m)

    c = Camioneta("azul", 4, 150, 1200, 70)
    print(c)
